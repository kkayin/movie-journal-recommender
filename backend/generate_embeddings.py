import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

df = pd.read_csv("movies.csv")
print(f"Loaded {len(df)} movies from movies.csv")

print("Loading SBERT model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Generating embeddings...")
overviews = df["overview"].tolist()
embeddings = model.encode(overviews, show_progress_bar=True)

np.save("movie_embeddings.npy", embeddings)

print(f"Done! Saved {len(df)} embeddings to  movie_embeddings.npy")


