"""
YEScape 2.0

Signal 5

Salary Reasonableness

Phase 3.5.4
"""

import re


class SalaryValidator:

    def __init__(self):

        self.max_safe_monthly = 30000

    def extract_salary(self, text):

        text = text.replace(",", "")

        patterns = [

            r"₹\s*(\d+)",

            r"rs\.?\s*(\d+)",

            r"inr\s*(\d+)",

            r"(\d+)\s*per month",

            r"(\d+)\s*/month"

        ]

        for pattern in patterns:

            match = re.search(pattern, text.lower())

            if match:

                return int(match.group(1))

        return None

    def analyze(self, text):

        salary = self.extract_salary(text)

        if salary is None:

            return {

                "salary_found": False,

                "salary": None,

                "salary_score": 80,

                "reason": "No salary mentioned"

            }

        if salary <= 15000:

            score = 100
            reason = "Typical internship stipend"

        elif salary <= 30000:

            score = 90
            reason = "Reasonable internship stipend"

        elif salary <= 50000:

            score = 60
            reason = "Higher than average internship stipend"

        else:

            score = 20
            reason = "Potentially unrealistic salary"

        return {

            "salary_found": True,

            "salary": salary,

            "salary_score": score,

            "reason": reason

        }


if __name__ == "__main__":

    validator = SalaryValidator()

    samples = [

        "Internship stipend ₹12000 per month",

        "Monthly stipend ₹25000",

        "Earn ₹50000 per month",

        "Amazing internship with ₹100000 monthly salary",

        "Google Internship 2027"

    ]

    for sample in samples:

        print()

        print(validator.analyze(sample))