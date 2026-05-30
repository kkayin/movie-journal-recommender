import random

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

# Multiple templates per situation so explanations feel varied
THEME_TEMPLATES = [
    "Your journal reflects {emotion_desc}. This film's exploration of {themes} mirrors the emotional undercurrent of your entry.",
    "Matched because your writing carries a tone of {emotion_desc}. The narrative themes of {themes} in this film closely align with where you are emotionally.",
    "Your entry suggests {emotion_desc}. This film resonates through its themes of {themes}, offering a cinematic reflection of your current state.",
]

FALLBACK_TEMPLATES = [
    "Your journal reflects {emotion_desc}. The emotional atmosphere of this film aligns with your current state of mind in ways that go beyond surface themes.",
    "Matched on emotional resonance — your writing carries a tone of {emotion_desc}, and this film's narrative arc mirrors that sentiment.",
    "Your entry suggests {emotion_desc}. While the themes aren't explicit, the emotional DNA of this film closely matches your journal's tone.",
]

def find_overlapping_themes(emotion: str, movie_overview: str) -> list:
    themes = EMOTION_THEMES.get(emotion, [])
    overview_lower = movie_overview.lower()
    return [theme for theme in themes if theme in overview_lower]

def generate_explanation(emotion: str, movie: dict, similarity_score: float) -> str:
    emotion_desc = EMOTION_DESCRIPTIONS.get(emotion, "a reflective state of mind")
    overlapping_themes = find_overlapping_themes(emotion, movie["overview"])

    if overlapping_themes:
        themes_str = " and ".join(overlapping_themes[:2])
        template = random.choice(THEME_TEMPLATES)
        explanation = template.format(
            emotion_desc=emotion_desc,
            themes=themes_str
        )
    else:
        template = random.choice(FALLBACK_TEMPLATES)
        explanation = template.format(emotion_desc=emotion_desc)

    return explanation

if __name__ == "__main__":
    test_movie = {
        "title": "Inside Out",
        "overview": "When 11-year-old Riley moves to a new city, her Emotions team up to help her through the transition.",
        "similarity_score": 0.823
    }

    for i in range(3):
        explanation = generate_explanation("sadness", test_movie, 0.823)
        print(f"Explanation {i+1}: {explanation}\n")