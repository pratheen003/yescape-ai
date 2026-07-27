"""
YEScape 2.0

Signal 5

Contact Information Validator

Phase 3.5.5
"""

import re


class ContactValidator:

    def __init__(self):
        pass

    def analyze(self, text):

        email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

        phone_pattern = r"(\+91[\-\s]?)?[6-9]\d{9}"

        website_pattern = r"(https?://\S+|www\.\S+)"

        email = re.findall(email_pattern, text)

        phone = re.findall(phone_pattern, text)

        website = re.findall(website_pattern, text)

        score = 0

        if email:
            score += 40

        if phone:
            score += 30

        if website:
            score += 30

        return {

            "emails_found": email,

            "phone_found": len(phone) > 0,

            "website_found": len(website) > 0,

            "contact_score": score

        }


if __name__ == "__main__":

    validator = ContactValidator()

    samples = [

        """
        Contact us:

        hr@google.com

        +91 9876543210

        https://careers.google.com
        """,

        """
        Congratulations!

        You have been selected.

        Reply immediately.
        """

    ]

    for sample in samples:

        print()

        print(validator.analyze(sample))