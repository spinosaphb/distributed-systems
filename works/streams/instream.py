import io
from entities.person import Person
from typing import List


class PeopleInputStream(io.IOBase):
    def __init__(self, people: List[str], is_: io.IOBase):
        self.people = people
        self.is_ = is_

    def read_system(self):
        name = input("Enter the person's name:")
        cpf = float(input("Enter the person's cpf:"))
        age = int(input("Enter the person's age:"))

        self.people[0] = Person(name, cpf, age)
        return self.people

    def read_file(self):
        return self.people

    def read_tcp(self):
        return self.people

    def read(self, size=-1):
        # Implement this method if needed, but it's not clear how it should behave in your context.