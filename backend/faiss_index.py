import numpy as np
import faiss
import pandas as pd

df = pd.read_csv("movies.csv")
movie_embeddings = np.load("movie_embeddings.npy").astype("float32")

dimension = movie_embeddings.shape[1]

print("Building Faiss index...")
index = faiss.IndexFlatIP(dimension)

faiss.normalize_L2(movie_embeddings)

index.add(movie_embeddings)
print(f"Added {index.ntotal} movie embeddings to the Faiss index.")

faiss.write_index(index, "movie_index.faiss")
print("Faiss index saved to movie_index.faiss")

def load_index():
    index = faiss.read_index("movie_index.faiss")
    return index

def search_similar_movies(journal_embedding, top_k=3):
    index = load_index()

    query = np.array([journal_embedding]).astype("float32")
    faiss.normalize_L2(query)

    scores, indices = index.search(query, top_k)

    results = []
    for i, idx in enumerate(indices[0]):
        movie = df.iloc[idx]
        results.append({
            "title": movie["title"],
            "overview": movie["overview"],
            "poster_path": movie["poster_path"],
            "vote_average": movie["vote_average"],
            "similarity_score": round(float(scores[0][i]), 3)
        })

    return results

if __name__ == "__main__":
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-MiniLM-L6-v2")
    test_journal = "I just want to feel happy and go on an adventure. I love discovering new things and meeting new people."
    embedding = model.encode(test_journal)

    results = search_similar_movies(embedding)
    for movie in results:
        print(f"{movie['title']} (Similarity: {movie['similarity_score']})")