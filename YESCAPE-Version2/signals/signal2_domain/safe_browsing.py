"""
YEScape 2.0

Signal 2

Google Safe Browsing

Phase 3.2.6
"""

import requests

from config.api_keys import GOOGLE_SAFE_BROWSING_API


class SafeBrowsingChecker:

    def __init__(self):

        self.endpoint = (

            "https://safebrowsing.googleapis.com/v4/threatMatches:find"

        )

    def check_url(self, url):

        payload = {

            "client": {

                "clientId": "YEScape",

                "clientVersion": "2.0"

            },

            "threatInfo": {

                "threatTypes": [

                    "MALWARE",

                    "SOCIAL_ENGINEERING",

                    "UNWANTED_SOFTWARE"

                ],

                "platformTypes": [

                    "ANY_PLATFORM"

                ],

                "threatEntryTypes": [

                    "URL"

                ],

                "threatEntries": [

                    {

                        "url": url

                    }

                ]

            }

        }

        response = requests.post(

            self.endpoint,

            params={

                "key": GOOGLE_SAFE_BROWSING_API

            },

            json=payload

        )

        data = response.json()

        if "matches" in data:

            return {

                "url": url,

                "safe": False,

                "matches": data["matches"],

                "safe_browsing_score": 0

            }

        return {

            "url": url,

            "safe": True,

            "matches": [],

            "safe_browsing_score": 100

        }


if __name__ == "__main__":

    checker = SafeBrowsingChecker()

    test_urls = [

        "https://google.com",

        "https://amazon.jobs",

        "https://microsoft.com"

    ]

    for url in test_urls:

        print()

        print(checker.check_url(url))