from fastapi import FastAPI
from pydantic import BaseModel
from emotion_classifier import analyze_journal

app = FastAPI()

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
