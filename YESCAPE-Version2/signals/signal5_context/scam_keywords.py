"""
YEScape 2.0

Signal 5

Scam Keyword Detection

Phase 3.5.1
"""


class ScamKeywordDetector:

    def __init__(self):

        self.keywords = [

            "registration fee",
            "processing fee",
            "security deposit",
            "pay now",
            "urgent hiring",
            "limited seats",
            "act immediately",
            "wire transfer",
            "upi payment",
            "bank transfer",
            "guaranteed job",
            "100% placement",
            "easy money",
            "quick earning",
            "instant joining",
            "selected immediately",
            "offer expires today",
            "no interview",
            "earn from home",
            "investment required"

        ]

    def analyze(self, text):

        text = text.lower()

        matched = []

        for keyword in self.keywords:

            if keyword in text:

                matched.append(keyword)

        score = max(0, 100 - (len(matched) * 15))

        return {

            "matched_keywords": matched,

            "keyword_count": len(matched),

            "scam_keyword_score": score

        }


if __name__ == "__main__":

    detector = ScamKeywordDetector()

    samples = [

        """
        Congratulations.

        You are selected.

        Please pay the registration fee immediately.

        Limited seats.

        Offer expires today.
        """,

        """
        Google Internship 2027

        Applications are open.

        Apply through the official careers portal.
        """

    ]

    for sample in samples:

        print()

        print(detector.analyze(sample))