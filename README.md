# CineFeels

A movie recommendation system that maps personal journal entries to emotionally resonant films using NLP and semantic search.

## Project Goal

Journal to Film analyzes the emotional tone of a user's journal entry and recommends films that match their current state of mind — explaining why each film was chosen.

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
- **Data:** TMDB API (997 films)

## Known Limitations

The explanation layer currently uses keyword matching for theme detection. A future improvement would replace this with semantic embedding similarity.
UX Design to be improved as well.