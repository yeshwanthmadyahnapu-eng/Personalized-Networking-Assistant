from fastapi import APIRouter
from backend.models import UserProfile, EventDetails
from ai_models.theme_extractor import extract_theme
from ai_models.conversation_generator import generate_conversation
from ai_models.fact_checker import fact_check

from backend.utils import (
    save_history,
    load_history,
    save_feedback,
    load_feedback
)
router = APIRouter()

user_profiles = []

@router.get("/hello")
def hello():
    return {"message": "Routes are working!"}


@router.post("/user")
def create_user(user: UserProfile):
    user_profiles.append(user)
    return {
        "message": "User profile created successfully",
        "data": user
    }


@router.get("/users")
def get_users():
    return user_profiles


@router.post("/analyze")
def analyze_event(event: EventDetails):
    return extract_theme(event.description)


@router.post("/generate")
def generate(event: EventDetails):

    theme = extract_theme(event.description)

    conversation = generate_conversation(
        theme["theme"],
        "Professional"
    )

    result = {
        "theme": theme["theme"],
        "conversation": conversation
    }

    save_history({
        "title": event.title,
        "description": event.description,
        "theme": theme["theme"],
        "conversation": conversation
    })

    return result


@router.get("/fact-check/{topic}")
def verify(topic: str):
    return fact_check(topic)

@router.get("/history")
def history():
    return load_history()

@router.post("/feedback")
def feedback(data: dict):
    save_feedback(data)
    return {"message": "Feedback saved successfully"}


@router.get("/feedback")
def get_feedback():
    from backend.utils import load_feedback
    return load_feedback()
