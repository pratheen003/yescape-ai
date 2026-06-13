def calculate_confidence(

    score,
    trust_data,
    positives,
    negatives

):

    confidence = 20

    evidence_count = (
        len(positives)
        +
        len(negatives)
    )

    confidence += evidence_count * 4

    confidence += abs(
        score - 50
    ) * 0.3

    confidence += abs(
        trust_data["overall_trust"] - 50
    ) * 0.3

    confidence = min(
        confidence,
        100
    )

    if confidence >= 85:

        explanation = (
            "Strong evidence supports this verdict."
        )

    elif confidence >= 65:

        explanation = (
            "Moderate evidence supports this verdict."
        )

    else:

        explanation = (
            "Limited evidence available. Results may change with more information."
        )

    return {

        "confidence": round(confidence),

        "evidence_count": evidence_count,

        "explanation": explanation

    }