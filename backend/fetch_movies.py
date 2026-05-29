import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")
print(f"Using TMDB API Key: {API_KEY}")
def fetch_movies(num_pages=50):
    movies = []
    for page in range(1, num_pages + 1):
        url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page={page}"
        response = requests.get(url)
        data = response.json()

        for movie in data["results"]:
            if movie.get("overview"):
                movies.append({
                    "title": movie["title"],
                    "overview": movie["overview"],
                    "poster_path": movie["poster_path"],
                    "vote_average": movie["vote_average"],
                    "genre_ids": movie["genre_ids"]
                })
        
        print(f"Fetched page {page}/{num_pages}")

    return movies

if __name__ == "__main__":
    movies = fetch_movies(num_pages=50)
    df = pd.DataFrame(movies)
    df.to_csv("movies.csv", index=False)
    print(f"Saved {len(df)} movies to movies.csv")




