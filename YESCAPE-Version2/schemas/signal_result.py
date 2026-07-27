"""
YEScape 2.0

Signal Result Schema

Phase 4.1.2
"""

from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class SignalResult:
    """
    Standard output produced by every signal.
    """

    signal_name: str

    score: float

    success: bool = True

    reason: str = ""

    details: Dict[str, Any] = field(default_factory=dict)