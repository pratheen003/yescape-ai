"""
YEScape 2.0

Signal 3

Company Name Extraction

Phase 3.3.1
"""

import re


class CompanyExtractor:

    def __init__(self):
        pass

    def extract(self, company_profile):

        if company_profile is None:
            return None

        company_profile = company_profile.strip()

        if company_profile == "":
            return None

        first_line = company_profile.split("\n")[0].strip()

        stop_words = [
            " is ",
            " was ",
            " are ",
            " provides ",
            " provide ",
            " develops ",
            " develop ",
            " specializes ",
            " specialise ",
            " specializes in ",
            " leading ",
            " global ",
            " multinational "
        ]

        company = first_line

        for word in stop_words:
            if word.lower() in company.lower():
                company = company[:company.lower().find(word.lower())]
                break

        company = company.strip(" ,.-:")

        return company


if __name__ == "__main__":

    sample = """
Google is a multinational technology company specializing
in Internet-related services.
"""

    extractor = CompanyExtractor()

    print(extractor.extract(sample))