"""
YEScape 2.0

Signal 3

Company Registry Loader

Phase 3.3.2
"""

import pandas as pd
from pathlib import Path


class CompanyRegistry:

    def __init__(self):

        file_path = Path(__file__).parent / "company_registry.csv"

        self.registry = pd.read_csv(file_path)

    def get_company(self, company_name):

        result = self.registry[
            self.registry["company"].str.lower()
            ==
            company_name.lower()
        ]

        if result.empty:
            return None

        return result.iloc[0].to_dict()


if __name__ == "__main__":

    registry = CompanyRegistry()

    print(registry.get_company("Google"))

    print(registry.get_company("Zoho"))

    print(registry.get_company("Microsoft"))