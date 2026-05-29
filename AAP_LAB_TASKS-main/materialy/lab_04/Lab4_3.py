import numpy as np

def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def semantic_search(query_vec, database, top_k=3):
    results = []
    for title, vec in database.items():
        sim = cosine_similarity(query_vec, vec)
        results.append((title, sim))
    
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:top_k]

def main():
    filmy = {
        "Incepcja":          np.array([0.8, 0.3, 0.9]),
        "Matrix":            np.array([0.75, 0.35, 0.85]),
        "Toy Story":         np.array([0.2, 0.9, 0.1]),
        "Shrek":             np.array([0.25, 0.85, 0.15]),
        "Szeregowiec Ryan":  np.array([0.6, 0.1, 0.7]),
    }

    query = np.array([0.7, 0.3, 0.8])
    
    print("Filmy najbardziej podobne do wektora: [0.7, 0.3, 0.8]\\n")
    results = semantic_search(query, filmy, top_k=3)
    
    for title, sim in results:
        print(f"{title}: {sim:.3f}")

if __name__ == "__main__":
    main()