def analyze_context(user_input):
    """
    This function understands WHAT the user is talking about.
    It classifies the problem into a context type.
    """

    text = user_input.lower()
    context = {}

    if any(word in text for word in ["job", "career", "salary", "company"]):
        context["type"] = "career"

    elif any(word in text for word in ["study", "college", "course", "degree"]):
        context["type"] = "education"

    elif any(word in text for word in ["hackathon", "competition", "contest"]):
        context["type"] = "opportunity"

    elif any(word in text for word in ["startup", "business", "idea"]):
        context["type"] = "startup"

    else:
        context["type"] = "general"

    context["original_input"] = user_input
    return context
