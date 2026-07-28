"""
YEScape 2.0

Verification Result Schema

Phase 4.3.8
"""

from dataclasses import dataclass, field
from typing import List

from schemas.signal_result import SignalResult


@dataclass
class VerificationResult:
    """
    Final verification result produced by the Verification Engine.
    """

    # -----------------------------
    # Final Decision
    # -----------------------------

    final_score: float = 0.0

    risk_level: str = ""

    risk_color: str = ""

    confidence: float = 0.0

    reasons: List[str] = field(default_factory=list)

    # -----------------------------
    # Individual Signal Results
    # -----------------------------

    signals: List[SignalResult] = field(default_factory=list)