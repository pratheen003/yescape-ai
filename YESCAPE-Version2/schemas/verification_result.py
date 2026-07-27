"""
YEScape 2.0

Verification Result Schema

Phase 4.1.3
"""

from dataclasses import dataclass, field
from typing import List

from schemas.signal_result import SignalResult


@dataclass
class VerificationResult:
    """
    Final verification result produced by the engine.
    """

    overall_score: float = 0

    confidence: float = 0

    verdict: str = ""

    explanation: List[str] = field(default_factory=list)

    signals: List[SignalResult] = field(default_factory=list)