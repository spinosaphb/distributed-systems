#message.py
from dataclasses import dataclass
import pickle

@dataclass
class Message:
    message: str
    required_response: bool = True

    @property
    def serialized(self) -> bytes:
        return pickle.dumps(self)

    @classmethod
    def from_bytes(cls, serialized) -> 'Message':
        return pickle.loads(serialized)
