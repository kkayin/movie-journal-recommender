import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("movies.csv")
movie_embeddings = np.load("movie_embeddings.npy")

def get_recommendations(journal_embedding, top_k=3):

    journal_vector = journal_embedding.reshape(1, -1)
    
    similarities = cosine_similarity(journal_vector, movie_embeddings)[0]

    top_indices = np.argsort(similarities)[::-1][:top_k]

    results = []
    for idx in top_indices:
        movie = df.iloc[idx]
        results.append({
            "title": movie["title"],
            "overview": movie["overview"],
            "poster_path": movie["poster_path"],
            "vote_average": movie["vote_average"],
            "similarity": round(float(similarities[idx]), 3)
        })

    return results

if __name__ == "__main__":
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-MiniLM-L6-v2")
    test_journal = "I just want to feel happy and go on an adventure. I love discovering new things and meeting new people."
    embedding = model.encode(test_journal)

    recommendations = get_recommendations(embedding)
    for movie in recommendations:
        print(f"{movie['title']} (Similarity: {movie['similarity']})")
