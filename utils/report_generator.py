from reportlab.platypus import (
    SimpleDocTemplate,
    Spacer,
    Paragraph,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime, timedelta

ist_time = datetime.utcnow() + timedelta(hours=5, minutes=30)


def generate_report(
    filename,
    score,
    status,
    verdict,
    positives,
    negatives,
    confidence_data,
    trust_data,
    reasoning,
    company="Unknown",
    company_status="Unknown",
    domain_reputation="Unknown",
    domain_age=None,
    https_status=False
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    # -------------------------
    # TITLE
    # -------------------------

    story.append(
        Paragraph(
            "YESCAPE AI VERIFICATION REPORT",
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            f"Generated: {ist_time.strftime('%d %b %Y | %I:%M %p IST')}",
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1, 20)
    )

    # -------------------------
    # SCORE SUMMARY
    # -------------------------

    story.append(
        Paragraph(
            "Trust Summary",
            styles["Heading1"]
        )
    )

    story.append(
        Paragraph(
            f"""
            <b>YES Score:</b> {score}/100<br/>
            <b>Status:</b> {status}<br/>
            <b>Positive Signals:</b> {len(positives)}<br/>
            <b>Negative Signals:</b> {len(negatives)}
            """,
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>AI Verdict:</b> {verdict}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>AI Confidence:</b> {confidence_data['confidence']}%",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Evidence Count:</b> {confidence_data['evidence_count']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Explanation:</b> {confidence_data['explanation']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            "<b>Trust Breakdown</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            f"""
            Company Trust: {trust_data.get('company_trust','N/A')}<br/>
            Recruiter Trust: {trust_data.get('recruiter_trust','N/A')}<br/>
            Website Trust: {trust_data.get('website_trust','N/A')}<br/>
            Language Trust: {trust_data.get('language_trust','N/A')}<br/>
            Context Trust: {trust_data.get('context_trust','N/A')}<br/>
            Overall Trust: {trust_data.get('overall_trust','N/A')}
            """,
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1, 10)
    )

    story.append(
        Paragraph(
            "<b>AI Reasoning</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            reasoning.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1, 20)
    )

    # -------------------------
    # COMPANY RESEARCH
    # -------------------------

    if domain_age:

        years = f"{round(domain_age / 365, 1)} Years"

        https_text = (
            "Enabled"
            if https_status
            else "Not Enabled"
        )

    else:

        years = "Not Available"

        https_text = "Not Applicable"

    story.append(
        Paragraph(
            "Company Research",
            styles["Heading1"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Company:</b> {company}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Status:</b> {company_status}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Domain Reputation:</b> {domain_reputation}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Domain Age:</b> {years} ",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>HTTPS:</b> {https_text}",
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1, 20)
    )

    # -------------------------
    # POSITIVE SIGNALS
    # -------------------------

    story.append(
        Paragraph(
            "Green Flags",
            styles["Heading1"]
        )
    )

    positives = list(dict.fromkeys(positives))
    negatives = list(dict.fromkeys(negatives))

    for item in positives:

        story.append(
            Paragraph(
                f"✓ {item}",
                styles["BodyText"]
            )
        )

    story.append(
        Spacer(1, 20)
    )

    # -------------------------
    # NEGATIVE SIGNALS
    # -------------------------

    story.append(
        Paragraph(
            "Red Flags",
            styles["Heading1"]
        )
    )

    for item in negatives:

        story.append(
            Paragraph(
                f"⚠ {item}",
                styles["BodyText"]
            )
        )

    story.append(
        Spacer(1, 20)
    )

    # -------------------------
    # FINAL VERDICT
    # -------------------------

    story.append(
        Paragraph(
            "Final Recommendation",
            styles["Heading1"]
        )
    )

    story.append(
        Paragraph(
            verdict,
            styles["BodyText"]
        )
    )

    doc.build(story)