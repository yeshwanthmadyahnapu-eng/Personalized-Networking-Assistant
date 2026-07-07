import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Personalized Networking Assistant",
    page_icon="🤝",
    layout="wide"
)

# ---------------- Session State ----------------

if "conversation_result" not in st.session_state:
    st.session_state.conversation_result = None

if "theme_result" not in st.session_state:
    st.session_state.theme_result = None

if "fact_result" not in st.session_state:
    st.session_state.fact_result = None

if "history_data" not in st.session_state:
    st.session_state.history_data = None

if "feedback_data" not in st.session_state:
    st.session_state.feedback_data = None

# ---------------- Title ----------------

st.title("🤝 Personalized Networking Assistant")
st.write("Generate personalized networking conversation starters using AI.")

# ---------------- User Profile ----------------

st.header("👤 User Profile")

name = st.text_input("Name")
profession = st.text_input("Profession")
skills = st.text_input("Skills (comma separated)")
interests = st.text_input("Interests (comma separated)")
bio = st.text_area("Short Bio")

if st.button("💾 Save Profile"):

    response = requests.post(
        f"{BASE_URL}/user",
        json={
            "name": name,
            "profession": profession,
            "skills": [x.strip() for x in skills.split(",") if x.strip()],
            "interests": [x.strip() for x in interests.split(",") if x.strip()],
            "bio": bio
        }
    )

    if response.status_code == 200:
        st.success("✅ User Profile Saved Successfully")
    else:
        st.error("Unable to save profile.")

# ---------------- Event ----------------

st.header("📅 Event Details")

title = st.text_input("Event Title")
description = st.text_area("Event Description")

col1, col2 = st.columns(2)

with col1:
    analyze = st.button("Analyze Theme")

with col2:
    generate = st.button("Generate Conversation")

col4, col5 = st.columns(2)

with col4:
    history = st.button("Conversation History")

with col5:
    feedback_history = st.button("Feedback History")

# ---------------- Theme ----------------

if analyze:

    response = requests.post(
        f"{BASE_URL}/analyze",
        json={
            "title": title,
            "description": description
        }
    )

    if response.status_code == 200:

        st.session_state.theme_result = response.json()

if st.session_state.theme_result:

    st.success("Theme Detected")

    st.info(
        f"Theme : {st.session_state.theme_result['theme']}"
    )

    st.write(
        f"Confidence : {st.session_state.theme_result['confidence']}"
    )

# ---------------- Generate Conversation ----------------

if generate:

    response = requests.post(
        f"{BASE_URL}/generate",
        json={
            "title": title,
            "description": description
        }
    )

    if response.status_code == 200:

        st.session_state.conversation_result = response.json()

# ---------------- Conversation Result ----------------

if st.session_state.conversation_result:

    result = st.session_state.conversation_result

    st.success("Conversation Generated Successfully")

    st.subheader("🎯 Detected Theme")
    st.info(result["theme"])

    st.subheader("💬 Networking Conversation Starters")

    starters = result["conversation"].split("\n")

    for starter in starters:
        if starter.strip():
            st.markdown(f"✅ {starter}")

    st.divider()

    st.subheader("⭐ Feedback")

    rating = st.slider(
        "Rate the generated conversation",
        min_value=1,
        max_value=5,
        value=5,
        key="rating_slider"
    )

    comments = st.text_area(
        "Comments",
        key="feedback_comments"
    )

    if st.button("Submit Feedback"):

        response = requests.post(
            f"{BASE_URL}/feedback",
            json={
                "theme": result["theme"],
                "rating": rating,
                "comments": comments
            }
        )

        if response.status_code == 200:
            st.success("✅ Feedback Saved Successfully!")

# ---------------- Fact Check ----------------

st.divider()
st.subheader("📖 Fact Checker")

col1, col2 = st.columns([4,1])

with col1:
    topic = st.text_input(
        "Enter Topic to Verify",
        key="fact_topic"
    )

with col2:
    check_fact = st.button("🔍 Check")

if check_fact:

    if topic.strip():

        response = requests.get(
            f"{BASE_URL}/fact-check/{topic}"
        )

        if response.status_code == 200:
            st.session_state.fact_result = response.json()

    else:
        st.warning("Please enter a topic.")

if st.session_state.fact_result:

    fact = st.session_state.fact_result

    st.subheader("📖 Fact Check Result")

    st.success(fact["status"])

    if "summary" in fact:
        st.write(fact["summary"])

    elif "options" in fact:
        st.write("Possible Topics:")
        for option in fact["options"]:
            st.write("•", option)

# ---------------- Conversation History ----------------

if history:

    response = requests.get(f"{BASE_URL}/history")

    if response.status_code == 200:
        st.session_state.history_data = response.json()

if "history_data" in st.session_state and st.session_state.history_data:

    st.divider()
    st.header("📜 Conversation History")

    for item in reversed(st.session_state.history_data):

        st.markdown("---")

        st.write("**Event Title:**", item["title"])
        st.write("**Theme:**", item["theme"])

        starters = item["conversation"].split("\n")

        for starter in starters:
            if starter.strip():
                st.write(starter)

# ---------------- Feedback History ----------------

if feedback_history:

    response = requests.get(f"{BASE_URL}/feedback")

    if response.status_code == 200:
        st.session_state.feedback_data = response.json()

if st.session_state.feedback_data:

    st.divider()
    st.header("📝 Feedback History")

    if len(st.session_state.feedback_data) == 0:
        st.info("No Feedback Available")

    else:

        for item in reversed(st.session_state.feedback_data):

            st.markdown("---")

            st.write("**Theme:**", item["theme"])
            st.write("**Rating:** ⭐", item["rating"])
            st.write("**Comments:**", item["comments"])