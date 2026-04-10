def needs_handoff(answer_text: str, retrieved_docs: list) -> bool:
    if not retrieved_docs:
        return True

    low_confidence_phrases = [
        "ma ei leidnud",
        "ei ole kindlat vastust",
        "küsimus suunatakse edasi",
    ]

    lowered = answer_text.lower()
    return any(p in lowered for p in low_confidence_phrases)