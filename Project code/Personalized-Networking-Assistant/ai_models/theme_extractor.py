from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

labels = [
    "Artificial Intelligence",
    "Machine Learning",
    "Data Science",
    "Cloud Computing",
    "Cybersecurity",
    "Software Development",
    "Networking",
    "Business",
    "Marketing",
    "Healthcare",
    "Finance",
    "Education"
]

def extract_theme(event_description: str):
    result = classifier(event_description, labels)

    return {
        "theme": result["labels"][0],
        "confidence": round(result["scores"][0], 2)
    }