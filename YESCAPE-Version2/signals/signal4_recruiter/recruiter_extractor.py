"""
YEScape 2.0

Signal 4

Recruiter Information Extraction

Phase 3.4.1
"""

import re


class RecruiterExtractor:

    EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    def extract_email(self, text):

        matches = re.findall(self.EMAIL_PATTERN, text)

        if matches:

            return matches[0]

        return None


if __name__ == "__main__":

    extractor = RecruiterExtractor()

    samples = [

        """
        Contact:

        John Smith

        HR Manager

        Google

        johnsmith@google.com
        """,

        """
        Send resume to

        jobs@gmail.com
        """,

        """
        Amazon Hiring

        hr@amazon.jobs
        """,

        """
        Email us at

        recruitment@yahoo.com
        """

    ]

    for sample in samples:

        print()

        print(extractor.extract_email(sample))