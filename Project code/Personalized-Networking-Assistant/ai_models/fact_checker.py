import wikipedia

def fact_check(topic):
    try:
        summary = wikipedia.summary(topic, sentences=3)

        return {
            "status": "Verified",
            "summary": summary
        }

    except wikipedia.exceptions.DisambiguationError as e:
        return {
            "status": "Multiple Results",
            "options": e.options[:5]
        }

    except wikipedia.exceptions.PageError:
        return {
            "status": "Not Found",
            "summary": "No information available."
        }

    except Exception as e:
        return {
            "status": "Error",
            "summary": str(e)
        }