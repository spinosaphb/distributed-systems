#candidate.py
from dataclasses import dataclass

@dataclass
class Candidate:

    candidate_id: int
    name: str
    nvotes: int
