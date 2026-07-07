def generate_conversation(theme, profession):

    starters = {
        "Artificial Intelligence": [
            "What inspired you to work in Artificial Intelligence?",
            "Which AI project are you currently working on?",
            "How do you think Generative AI will change software development?",
            "Which AI tools or frameworks do you use most often?",
            "What skills should students develop to build a career in AI?"
        ],

        "Machine Learning": [
            "What machine learning project are you most proud of?",
            "Which ML framework do you use most frequently?",
            "How do you evaluate the performance of your ML models?",
            "What datasets do you enjoy working with?",
            "Which ML trend do you think has the biggest future?"
        ],

        "Cloud Computing": [
            "Which cloud platform do you work with the most?",
            "How has cloud computing improved your projects?",
            "What cloud certifications would you recommend?",
            "Which cloud service do you use every day?",
            "What advice would you give to someone learning cloud computing?"
        ],

        "Data Science": [
            "What data science project are you currently working on?",
            "Which visualization tools do you prefer?",
            "How do you clean large datasets efficiently?",
            "Which programming language do you use for data analysis?",
            "What trends in data science excite you the most?"
        ]
    }

    if theme in starters:
        conversations = starters[theme]
    else:
        conversations = [
            f"What interested you most about {theme}?",
            f"How are you applying {theme} in your current work?",
            f"What challenges have you faced while learning {theme}?",
            f"What emerging trends in {theme} excite you the most?",
            f"What advice would you give beginners interested in {theme}?"
        ]

    return "\n\n".join(
        [f"{i+1}. {text}" for i, text in enumerate(conversations)]
    )