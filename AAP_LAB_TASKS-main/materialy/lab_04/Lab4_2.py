from pymongo import MongoClient
import requests

def main():
    # 1. Połącz z MongoDB
    client = MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=5000)

    try:
        client.admin.command('ping')
    except Exception as e:
        print(f"Błąd: {e}")
        return

    db = client.lab4
    networks = db["networks"]
    networks.drop()

    # 2. Pobierz dane z API
    response = requests.get("https://api.geckoterminal.com/api/v2/networks")
    response.raise_for_status()
    data = response.json()["data"]

    # 3. Wstaw dokumenty
    if data:
        networks.insert_many(data)
        print(f"Zapisano {len(data)} sieci do bazy MongoDB.")
    else:
        print("Brak danych do zapisania.")

    # 4. Agregacja -- ile sieci per typ
    pipeline = [
        {"$group": {"_id": "$attributes.type", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]
    for doc in networks.aggregate(pipeline):
        print(f"Typ: {doc['_id']} -> Ilość: {doc['count']}")

if __name__ == "__main__":
    main()