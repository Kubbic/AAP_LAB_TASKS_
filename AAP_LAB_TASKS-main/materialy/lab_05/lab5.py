from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StringType
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

spark = SparkSession.builder \
    .appName("Chicago Crimes Analysis") \
    .getOrCreate()

df_crimes = spark.read.option("header", True).csv("chicago_crimes_sample.csv")

df_crimes = df_crimes.dropDuplicates()

df_crimes = df_crimes.dropna(subset=["id", "date", "primary_type", "location_description"])

df_crimes = df_crimes.withColumn("parsed_date", F.to_timestamp("date", "yyyy-MM-dd'T'HH:mm:ss.SSS"))
df_crimes = df_crimes.filter(F.col("parsed_date").isNotNull())
df_crimes = df_crimes.withColumn("hour", F.hour("parsed_date"))

@F.udf(returnType=StringType())
def classify_time_of_day(hour):
    if hour is None:
        return None
    if 6 <= hour < 18:
        return "dzien"
    elif 18 <= hour < 22:
        return "wieczor"
    else:
        return "noc"

df_crimes = df_crimes.withColumn("time_of_day", classify_time_of_day(F.col("hour")))

df_crimes = df_crimes.cache()

crime_categories = [
    ("THEFT", "Property Crime"),
    ("BATTERY", "Violent Crime"),
    ("CRIMINAL DAMAGE", "Property Crime"),
    ("ASSAULT", "Violent Crime"),
    ("DECEPTIVE PRACTICE", "White Collar Crime"),
    ("OTHER OFFENSE", "Other")
]
df_category = spark.createDataFrame(crime_categories, ["primary_type", "broad_category"])

df_crimes = df_crimes.join(F.broadcast(df_category), on="primary_type", how="left")

df_crimes.write.mode("overwrite").partitionBy("year").parquet("chicago_crimes_partitioned.parquet")

agg_location = df_crimes.groupBy("location_description", "primary_type") \
    .agg(F.count("id").alias("crime_count")) \
    .orderBy(F.col("crime_count").desc())

agg_location.show(10, truncate=False)

agg_time = df_crimes.groupBy("time_of_day", "primary_type") \
    .agg(F.count("id").alias("crime_count")) \
    .orderBy(F.col("crime_count").desc())

agg_time.show(10, truncate=False)

heavy_agg = df_crimes.groupBy("location_description", "time_of_day", "primary_type") \
    .agg(F.count("id").alias("crime_count")) \
    .orderBy(F.col("crime_count").desc())

heavy_agg.explain(True)

heavy_agg.show(10, truncate=False)

df_ml = df_crimes.select("primary_type", "location_description", "arrest", "domestic", "hour").dropna()

indexer_location = StringIndexer(inputCol="location_description", outputCol="location_index", handleInvalid="keep")
indexer_arrest = StringIndexer(inputCol="arrest", outputCol="arrest_index", handleInvalid="keep")
indexer_domestic = StringIndexer(inputCol="domestic", outputCol="domestic_index", handleInvalid="keep")
indexer_label = StringIndexer(inputCol="primary_type", outputCol="label", handleInvalid="keep")

assembler = VectorAssembler(
    inputCols=["location_index", "arrest_index", "domestic_index", "hour"],
    outputCol="features"
)

rf = RandomForestClassifier(labelCol="label", featuresCol="features", numTrees=10)

pipeline = Pipeline(stages=[indexer_location, indexer_arrest, indexer_domestic, indexer_label, assembler, rf])

train_data, test_data = df_ml.randomSplit([0.8, 0.2], seed=42)

model = pipeline.fit(train_data)
predictions = model.transform(test_data)

predictions.select("primary_type", "label", "prediction", "probability").show(5, truncate=False)

evaluator = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction", metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print(f"Accuracy: {accuracy:.4f}")