"""
YEScape 2.0

Signal 5

Advance Fee Detection

Phase 3.5.3
"""


class AdvanceFeeDetector:

    def __init__(self):

        self.fee_keywords = [

            "registration fee",
            "processing fee",
            "security deposit",
            "training fee",
            "joining fee",
            "payment required",
            "pay now",
            "upi",
            "bank transfer",
            "scan qr",
            "application fee",
            "deposit amount"

        ]

        self.negation_patterns = [

            "no",
            "not",
            "without",
            "free",
            "no fee",
            "no payment",
            "not required"

        ]

    def analyze(self, text):

        text = text.lower()

        matched = []

        for keyword in self.fee_keywords:

            if keyword in text:

                ignore = False

                for negation in self.negation_patterns:

                    if f"{negation} {keyword}" in text:

                        ignore = True
                        break

                if ignore:
                    continue

                matched.append(keyword)

        score = max(0, 100 - (len(matched) * 20))

        return {

            "matched_fee_keywords": matched,

            "fee_keyword_count": len(matched),

            "advance_fee_detected": len(matched) > 0,

            "advance_fee_score": score

        }


if __name__ == "__main__":

    detector = AdvanceFeeDetector()

    samples = [

        """
        Congratulations.

        Please pay the registration fee through UPI.

        Your processing fee must be completed today.
        """,

        """
        Google Internship 2027.

        No application fee is required.

        Apply through the official careers portal.
        """

    ]

    for sample in samples:

        print()

        print(detector.analyze(sample))