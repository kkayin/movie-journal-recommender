from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Movie Recommender API is running!"}
