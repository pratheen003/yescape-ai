"""
YEScape 2.0

Signal 5

Urgency Detection

Phase 3.5.2
"""


class UrgencyDetector:

    def __init__(self):

        self.urgency_words = [

            "urgent",

            "immediately",

            "today",

            "limited seats",

            "last date",

            "act now",

            "hurry",

            "within 24 hours",

            "offer expires",

            "instant joining",

            "first come first serve",

            "closing soon",

            "don't miss",

            "apply now"

        ]

    def analyze(self, text):

        text = text.lower()

        matched = []

        for word in self.urgency_words:

            if word in text:

                matched.append(word)

        score = max(0, 100 - (len(matched) * 15))

        return {

            "matched_urgency": matched,

            "urgency_count": len(matched),

            "urgency_score": score

        }


if __name__ == "__main__":

    detector = UrgencyDetector()

    samples = [

        """
        Hurry!

        Limited seats available.

        Offer expires today.

        Apply immediately.
        """,

        """
        Google Internship 2027

        Applications are open until August.

        Candidates may apply through the official website.
        """

    ]

    for sample in samples:

        print()

        print(detector.analyze(sample))