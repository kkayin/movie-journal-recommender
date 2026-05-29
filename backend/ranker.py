import numpy as np
import pandas as pd

df = pd.read_csv("movies.csv")

MIN_RATING = df["vote_average"].min()
MAX_RATING = df["vote_average"].max()

def normalize(value, min_val, max_val):
    """Normalize a value to the range [0, 1]"""
    if max_val == min_val: 
        return 0.0
    return (value - min_val) / (max_val - min_val)

def hybrid_rank(recommendations: list) -> list:
    # Filter out low quality movies first
    filtered = [r for r in recommendations if r["vote_average"] >= 6.5]
    
    # Fallback in case filtering removes everything
    if len(filtered) == 0:
        filtered = sorted(recommendations, key=lambda x: x["vote_average"], reverse=True)[:3]
    
    recommendations = filtered

    similarities = [r["similarity_score"] for r in recommendations]
    min_sim = min(similarities)
    max_sim = max(similarities)

    ratings = [r["vote_average"] for r in recommendations]
    min_rating = min(ratings)
    max_rating = max(ratings)

    for movie in recommendations:
        norm_similarity = normalize(movie["similarity_score"], min_sim, max_sim)
        norm_rating = normalize(movie["vote_average"], min_rating, max_rating)
        movie["hybrid_score"] = round(0.7 * norm_similarity + 0.2 * norm_rating + 0.1 * norm_similarity, 3)

    recommendations.sort(key=lambda x: x["hybrid_score"], reverse=True)
    return recommendations[:3]

if __name__ == "__main__":
    test_movies = [
        {"title": "Sex Trip", "similarity_score": 0.343, "vote_average": 6.0},
        {"title": "Alice in Wonderland", "similarity_score": 0.302, "vote_average": 6.6},
        {"title": "Interstellar", "similarity_score": 0.276, "vote_average": 8.475}
    ]

    ranked = hybrid_rank(test_movies)
    for movie in ranked:
        print(f"{movie['title']} - hybrid score: {movie['hybrid_score']}")
