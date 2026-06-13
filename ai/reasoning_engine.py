def generate_reasoning(

    status,
    positives,
    negatives

):

    reasons = []

    if status == "SAFE":

        intro = (
            "This internship appears legitimate because:"
        )

    elif status == "CAUTION":

        intro = (
            "This internship contains mixed signals:"
        )

    elif status == "RISKY":

        intro = (
            "This internship contains several warning signs:"
        )

    else:

        intro = (
            "This internship appears highly suspicious because:"
        )

    if positives:

        reasons.append(
            f"• {len(positives)} positive trust indicators were identified."
        )

    if negatives:

        reasons.append(
            f"• {len(negatives)} risk indicators were detected."
        )

    if "Recognized company mention" in " ".join(positives):

        reasons.append(
            "• A recognized company was identified in the offer."
        )

    if "Professional recruiter email" in " ".join(positives):

        reasons.append(
            "• The recruiter email appears professional and trustworthy."
        )

    if "Recruiter domain matches company" in " ".join(positives):

        reasons.append(
            "• The recruiter domain matches the claimed company."
        )

    if "No registration fee" in " ".join(positives):

        reasons.append(
            "• No payment requirement was detected."
        )

    reasoning = intro

    for reason in reasons:

        reasoning += "\n\n" + reason

    return reasoning