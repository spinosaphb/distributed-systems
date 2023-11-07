#user.py
from dataclasses import dataclass

@dataclass
class User:
    username: str
    password: str
    role: str

    def is_admin(self):
        return self.role == "admin"

    @classmethod
    def from_json(cls, json_list):
        return [cls(**user_info) for user_info in json_list["users"]]
