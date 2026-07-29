"""
YEScape 2.0

Verification Logger

Phase 4.4.4
"""

from datetime import datetime


class VerificationLogger:

    def log(self, message):

        current_time = datetime.now().strftime("%H:%M:%S")

        print(f"[{current_time}] {message}")