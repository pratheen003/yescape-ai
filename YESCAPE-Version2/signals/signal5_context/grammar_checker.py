"""
YEScape 2.0

Signal 5

Grammar Checker

Phase 3.5.6
"""

import language_tool_python
import textwrap


class GrammarChecker:

    def __init__(self):

        self.tool = language_tool_python.LanguageTool("en-US")

    def analyze(self, text):

        text = textwrap.dedent(text).strip()

        matches = []

        for m in self.tool.check(text):

            msg = m.message.lower()

            if "whitespace" in msg:
                continue

            if "typography" in msg:
                continue

            if "quotation mark" in msg:
                continue

            matches.append(m)

        error_count = len(matches)

        if error_count == 0:
            score = 100

        elif error_count <= 2:
            score = 95

        elif error_count <= 5:
            score = 90

        elif error_count <= 8:
            score = 80

        else:
            score = 70

        return {

            "grammar_errors": error_count,

            "grammar_score": score,

            "mistakes": [

                {

                    "message": m.message,

                    "context": m.context

                }

                for m in matches[:5]

            ]

        }


if __name__ == "__main__":

    checker = GrammarChecker()

    samples = [

        """
        Congratulations!

        You have been selected for Google's internship.

        Please visit our careers website.
        """,

        """
        Congratulation Dear Candidate!!!

        You are selected.

        Pay registration fee now.

        Hurry limited seat.
        """

    ]

    for sample in samples:

        print()

        print(checker.analyze(sample))