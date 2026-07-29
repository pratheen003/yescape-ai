"""
YEScape 2.0

Verification Pipeline

Phase 4.4.3
"""

from core.verification_engine import VerificationEngine
from core.logger.logger import VerificationLogger
import time


class VerificationPipeline:

    """
    Executes the complete verification pipeline.
    """

    def __init__(self):

        self.engine = VerificationEngine()

        self.logger = VerificationLogger()

    def execute(self, request):

        self.logger.log("Verification Pipeline Started")

        start_time = time.perf_counter()

        try:

            result = self.engine.verify(request)

            end_time = time.perf_counter()

            elapsed = round(end_time - start_time, 2)

            result.execution_time = elapsed

            self.logger.log("Verification Completed Successfully")

            self.logger.log(f"Execution Time : {elapsed} seconds")

            return result

        except Exception as e:

            self.logger.log("Pipeline Failed")

            self.logger.log(str(e))

            raise