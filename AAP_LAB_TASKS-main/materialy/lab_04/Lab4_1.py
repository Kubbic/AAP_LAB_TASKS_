import sqlite3
import requests

def main():
    # 1. Pobierz dane z API
    print("Pobieranie danych z API...")
    response = requests.get("https://randomuser.me/api/?results=30")
    response.raise_for_status()
    users = response.json()["results"]

    # 2. Stworz tabele Users (id, first_name, last_name, email, age, gender, country)
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT,
            age INTEGER,
            gender TEXT,
            country TEXT
        )
    ''')

    # 3. Wstaw dane z parametryzacja (? nie f-string!)
    user_data = []
    for u in users:
        first_name = u["name"]["first"]
        last_name = u["name"]["last"]
        email = u["email"]
        age = u["dob"]["age"]
        gender = u["gender"]
        country = u["location"]["country"]
        user_data.append((first_name, last_name, email, age, gender, country))

    cur.executemany('''
        INSERT INTO Users (first_name, last_name, email, age, gender, country)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', user_data)
    conn.commit()

    # 4. Zapytania analityczne
    print("=== Płeć ===")
    cur.execute("SELECT gender, COUNT(*) FROM Users GROUP BY gender")
    for row in cur.fetchall():
        print(f"  {row[0]}: {row[1]}")

    print("\\n=== Średni wiek ===")
    cur.execute("SELECT AVG(age) FROM Users")
    print(f"  {cur.fetchone()[0]:.1f} lat")

    print("\\n=== Kraje (ilość) ===")
    cur.execute("SELECT country, COUNT(*) FROM Users GROUP BY country ORDER BY COUNT(*) DESC")
    for row in cur.fetchall():
        print(f"  {row[0]}: {row[1]}")

    conn.close()

if __name__ == "__main__":
    main()