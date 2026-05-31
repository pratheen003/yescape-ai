from reportlab.platypus import (
    SimpleDocTemplate,
    Spacer,
    Paragraph
)

from reportlab.lib import colors
from reportlab.lib import styles
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
filename,
score,
status,
verdict,
positives,
negatives
):

    doc=SimpleDocTemplate(
    filename
    )

    stylesheets=getSampleStyleSheet()

    story=[]

    title=Paragraph(
    "YES-cape AI Verification Report",
    stylesheets["Title"]
    )

    story.append(title)

    story.append(
    Spacer(1,20)
    )


    story.append(

    Paragraph(
    f"<b>YES Score:</b> {score}/100",
    stylesheets["Heading2"]
    )
    )

    story.append(

    Paragraph(
    f"<b>Status:</b> {status}",
    stylesheets["Heading3"]
    )
    )


    story.append(

    Paragraph(
    f"<b>AI Verdict:</b> {verdict}",
    stylesheets["BodyText"]
    )
    )

    story.append(
    Spacer(1,20)
    )


    story.append(

    Paragraph(
    "Positive Signals",
    stylesheets["Heading2"]
    )
    )

    for item in positives:

        story.append(

        Paragraph(
        f"✔ {item}",
        stylesheets["BodyText"]
        )
        )


    story.append(
    Spacer(1,20)
    )


    story.append(

    Paragraph(
    "Risk Signals",
    stylesheets["Heading2"]
    )
    )


    for item in negatives:

        story.append(

        Paragraph(
        f"⚠ {item}",
        stylesheets["BodyText"]
        )
        )


    doc.build(story)