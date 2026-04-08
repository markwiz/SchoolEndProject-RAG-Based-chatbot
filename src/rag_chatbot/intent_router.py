def detect_intent(question: str) -> str:
    q = question.lower()

    if any(x in q for x in ["mis keeli", "milliseid keeli", "mis keelt", "keeled"]):
        return "languages"

    if any(x in q for x in ["kaua võtab", "kui kaua", "mitu kuud", "mitu aastat", "a1", "a2", "b1", "b2", "c1", "c2"]):
        return "learning_duration"

    if any(x in q for x in ["maks", "hind", "arve", "osamakse"]):
        return "billing"

    if any(x in q for x in ["registreeru", "registreeruda", "liituda"]):
        return "registration"

    return "general"