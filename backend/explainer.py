EMOTION_DESCRIPTIONS = {
    "joy": "excitement and a desire for celebration and adventure",
    "sadness": "emotional fatigue and a need for healing and reflection",
    "anger": "frustration and a desire for justice or resolution",
    "fear": "anxiety and uncertainty, seeking courage and escape",
    "surprise": "a sense of wonder and openness to the unexpected",
    "disgust": "disillusionment and a search for redemption",
    "neutral": "a reflective and contemplative state of mind"
}


EMOTION_THEMES = {
    "joy": ["celebration", "growth", "love", "adventure", "happiness"],
    "sadness": ["grief", "healing", "loss", "reflection", "recovery"],
    "anger": ["justice", "revenge", "conflict", "power", "resistance"],
    "fear": ["survival", "uncertainty", "danger", "courage", "escape"],
    "surprise": ["discovery", "mystery", "unexpected", "wonder"],
    "disgust": ["corruption", "betrayal", "moral conflict", "redemption"],
    "neutral": ["journey", "identity", "everyday life", "relationships"]
}

def find_overlapping_themes(emotion: str, movie_overview: str) -> list:
    """Find which emotional themes appear in the movie overview"""
    themes = EMOTION_THEMES.get(emotion, [])
    overview_lower = movie_overview.lower()
    
    overlapping = []
    for theme in themes:
        if theme in overview_lower:
            overlapping.append(theme)
    
    return overlapping

def generate_explanation(emotion: str, movie: dict, similarity_score: float) -> str:
    """Generate a human readable explanation for why this movie was recommended"""
    
    
    emotion_desc = EMOTION_DESCRIPTIONS.get(emotion, "a reflective state of mind")
    
    
    overlapping_themes = find_overlapping_themes(emotion, movie["overview"])
    
    
    if overlapping_themes:
        themes_str = " and ".join(overlapping_themes[:2])  # max 2 themes
        explanation = (
            f"Recommended because your journal reflects {emotion_desc}. "
            f"This film explores themes of {themes_str}, "
            f"closely mirroring the emotional narrative of your entry. "
            f"Semantic similarity: {similarity_score}"
        )
    else:
        explanation = (
            f"Recommended because your journal reflects {emotion_desc}. "
            f"The emotional tone of this film closely aligns with your current state of mind. "
            f"Semantic similarity: {similarity_score}"
        )
    
    return explanation

if __name__ == "__main__":
    test_movie = {
        "title": "Inside Out",
        "overview": "When 11-year-old Riley moves to a new city, her Emotions team up to help her through the transition. Joy, Fear, Anger, Disgust and Sadness work together.",
        "similarity_score": 0.823
    }
    
    explanation = generate_explanation("sadness", test_movie, 0.823)
    print(f"Movie: {test_movie['title']}")
    print(f"Explanation: {explanation}")