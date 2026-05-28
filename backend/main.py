from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from emotion_classifier import analyze_journal
from faiss_index import search_similar_movies
from explainer import generate_explanation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class JournalInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Movie Recommender API is running!"}

@app.post("/analyze-journal")
def analyze(input: JournalInput):
    result = analyze_journal(input.text)
    return {
        "emotion": result["emotion"],
        "confidence": result["confidence"],
        "themes": result["themes"]
    }

@app.post("/recommend")
def recommend(input: JournalInput):
    # Step 1: Analyze journal
    analysis = analyze_journal(input.text)
    emotion = analysis["emotion"]
    embedding = analysis["embedding"]

    # Step 2: Find similar movies via FAISS
    movies = search_similar_movies(embedding, top_k=3)

    # Step 3: Generate explanation for each movie
    recommendations = []
    for movie in movies:
        explanation = generate_explanation(emotion, movie, movie["similarity_score"])
        recommendations.append({
            "title": movie["title"],
            "overview": movie["overview"],
            "poster_path": movie["poster_path"],
            "vote_average": movie["vote_average"],
            "similarity_score": movie["similarity_score"],
            "explanation": explanation
        })

    return {
        "emotion": emotion,
        "confidence": analysis["confidence"],
        "themes": analysis["themes"],
        "recommendations": recommendations
    }