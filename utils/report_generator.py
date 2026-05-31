from reportlab.platypus import (
    SimpleDocTemplate,
    Spacer,
    Paragraph,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    filename,
    score,
    status,
    verdict,
    positives,
    negatives,
    company="Unknown",
    company_status="Unknown",
    domain_reputation="Unknown"
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
            f"<b>YES Score:</b> {score}/100",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Status:</b> {status}",
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
        Spacer(1, 20)
    )

    # -------------------------
    # COMPANY RESEARCH
    # -------------------------

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