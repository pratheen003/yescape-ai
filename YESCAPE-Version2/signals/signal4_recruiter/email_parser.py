"""
YEScape 2.0

Signal 4

Email Parser

Phase 3.4.2
"""


class EmailParser:

    def __init__(self):
        pass

    def parse(self, email):

        if email is None:

            return None

        email = email.strip().lower()

        if "@" not in email:

            return None

        username, domain = email.split("@", 1)

        return {

            "email": email,

            "username": username,

            "domain": domain

        }


if __name__ == "__main__":

    parser = EmailParser()

    emails = [

        "johnsmith@google.com",

        "jobs@gmail.com",

        "hr@amazon.jobs",

        "recruitment@yahoo.com",

        "careers@microsoft.com"

    ]

    for email in emails:

        print()

        print(parser.parse(email))