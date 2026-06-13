def analyze_context(text):

    text = text.lower()

    score = 0

    positives = []

    negatives = []

    safe_contexts_found = []

    risky_contexts_found = []

    # ------------------
    # SAFE CONTEXTS
    # ------------------

    safe_phrases = [

        "no registration fee",
        "free internship",
        "official company website",
        "selection based on interview",
        "interview process",
        "application deadline",
        "certificate provided after completion"

    ]

    for phrase in safe_phrases:

        if phrase in text:

            score += 5

            positives.append(
                f"Safe context detected: {phrase}"
            )

            safe_contexts_found.append(
                phrase
            )

    # ------------------
    # SCAM CONTEXTS
    # ------------------

    scam_phrases = [

        "pay before interview",
        "pay to apply",
        "payment required before selection",
        "instant selection",
        "guaranteed selection",
        "no interview required",
        "earn money immediately"

    ]

    for phrase in scam_phrases:

        if phrase in text:

            score -= 20

            negatives.append(
                f"Suspicious context detected: {phrase}"
            )

            risky_contexts_found.append(
                phrase
            )

    return {

        "score": score,

        "positives": positives,

        "negatives": negatives,

        "safe_contexts": safe_contexts_found,

        "negative_contexts": risky_contexts_found

    }