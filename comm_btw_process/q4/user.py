from dataclasses import dataclass
from enum import Enum


class role(Enum):
    admin = 1
    user = 2


@dataclass
class User:
    username: str
    password: str
    role: role

    def is_admin(self):
        return self.role == role.admin

    @classmethod
    def from_json(cls, json_list):
        return [cls(**user_info) for user_info in json_list["users"]]
