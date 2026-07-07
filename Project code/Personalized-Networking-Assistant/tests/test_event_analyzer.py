from ai_models.theme_extractor import extract_theme


def test_event_analysis_returns_theme():
    result = extract_theme(
        "Artificial Intelligence, Machine Learning and Cloud Computing conference."
    )

    assert isinstance(result, dict)
    assert "theme" in result
    assert "confidence" in result