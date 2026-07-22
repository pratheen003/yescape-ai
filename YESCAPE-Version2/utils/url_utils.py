"""
YEScape 2.0

URL Utility Functions

Shared across all verification signals.
"""

from urllib.parse import urlparse


class URLUtils:

    @staticmethod
    def normalize(url):

        """
        Normalize any website URL into a clean domain.

        Examples

        google.com
            -> google.com

        www.google.com
            -> google.com

        https://www.google.com/jobs
            -> google.com

        careers.google.com/jobs
            -> careers.google.com
        """

        url = url.strip().lower()

        if not url.startswith(("http://", "https://")):

            url = "https://" + url

        parsed = urlparse(url)

        domain = parsed.netloc

        if domain.startswith("www."):

            domain = domain[4:]

        return domain


if __name__ == "__main__":

    urls = [

        "google.com",

        "www.google.com",

        "https://google.com",

        "https://www.google.com",

        "https://careers.google.com/jobs",

        "amazon.jobs"

    ]

    for u in urls:

        print(u, "->", URLUtils.normalize(u))