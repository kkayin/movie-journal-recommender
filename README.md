# 🎬 CineFeels

A movie recommendation system that maps personal journal entries to emotionally resonant films using NLP and semantic search.

## Project Goal

CineFeels analyzes the emotional tone of a user's journal entry and recommends films that match their current state of mind — explaining why each film was chosen.

## Features

- Write a journal entry and receive 3 emotionally matched film recommendations
- Detects your emotional state (joy, sadness, anger, fear, surprise, disgust) with confidence score
- Each recommendation includes a movie poster, rating, synopsis, and personalized explanation
- Rate each recommendation 1–5 stars to provide feedback on relevance
- Emotion tags displayed so users understand what themes drove the recommendations

## Architecture

- **Frontend (React):** Journal input, emotion display, movie recommendations with posters and explanations, star rating feedback
- **Backend (Python):** Emotion classification, semantic embedding, vector search, hybrid ranking
- **Communication:** REST API over localhost

## Quick Start

Requirements: Python 3.11+, Node.js

```bash
# Terminal 1 - Backend (http://localhost:8000)
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

# Terminal 2 - Frontend (http://localhost:5173)
cd frontend
npm install
npm run dev
```

## Technologies

- **Frontend:** React, Tailwind CSS, Vite
- **Backend:** Python, FastAPI, HuggingFace Transformers, Sentence-Transformers, FAISS, scikit-learn
- **Data:** TMDB API 

## Known Limitations

The explanation layer currently uses keyword matching for theme detection. A future improvement would replace this with semantic embedding similarity. UX design to be improved as well.