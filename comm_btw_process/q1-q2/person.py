from dataclasses import dataclass

@dataclass
class Person:
    name: str
    cpf: str
    age: str

    @property
    def byte_name(self):
        return bytes(self.name, encoding="utf-8")

    def __str__(self) -> str:
        import sys
        name_byte_size = sys.getsizeof(self.byte_name)
        return f"{name_byte_size},{self.name},{self.cpf},{self.age}"