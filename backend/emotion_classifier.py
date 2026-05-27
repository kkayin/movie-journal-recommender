from transformers import pipeline
from sentence_transformers import SentenceTransformer

# Load models
print("Loading emotion model...")
emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=1
)

print("Loading SBERT model...")
sbert_model = SentenceTransformer('all-MiniLM-L6-v2')

# Emotion to theme mapping
EMOTION_THEMES = {
    "joy": ["celebration", "growth", "love", "adventure", "happiness"],
    "sadness": ["grief", "healing", "loss", "reflection", "recovery"],
    "anger": ["justice", "revenge", "conflict", "power", "resistance"],
    "fear": ["survival", "uncertainty", "danger", "courage", "escape"],
    "surprise": ["discovery", "mystery", "unexpected", "wonder"],
    "disgust": ["corruption", "betrayal", "moral conflict", "redemption"],
    "neutral": ["journey", "identity", "everyday life", "relationships"]
}

def analyze_journal(text: str):
    # Get emotion
    result = emotion_model(text)
    emotion = result[0][0]["label"].lower()
    confidence = result[0][0]["score"]

    # Get themes for that emotion
    themes = EMOTION_THEMES.get(emotion, ["journey", "identity"])

    # Get embedding
    embedding = sbert_model.encode(text)

    return {
        "emotion": emotion,
        "confidence": round(confidence, 3),
        "themes": themes,
        "embedding": embedding
    }

# Test it
if __name__ == "__main__":
    test = "I've been feeling really overwhelmed lately. Everything feels too much and I just need a break."
    result = analyze_journal(test)
    print(f"Emotion: {result['emotion']} ({result['confidence']})")
    print(f"Themes: {result['themes']}")
    print(f"Embedding shape: {result['embedding'].shape}")