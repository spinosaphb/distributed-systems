import io
from typing import List

import dataclasses
from dataclasses import dataclass
from person import Person
from streams.utils import from_data
from client import client
from pprint import pprint
from typing import Optional


@dataclass
class PeopleInputStream(io.IOBase):
    people: List[Person] = dataclasses.field(default_factory=list)

    def read(self):
        pass


class PersonInputPrintStream(PeopleInputStream):

    def read(self):
        print("Reading data from the console or input source")

        while True:
            print("Press enter to stop reading")
            name = input("Name: ")
            if not name:
                break
            cpf = input("CPF: ")
            age = input("Age: ")
            self.people.append(Person(name, cpf, age))

        pprint(self.people)


class PersonInputFileStream(PeopleInputStream):

    def read(self):

        with open("resources/people.txt", "r") as f:
            data = f.read()

        self.people = from_data(data)

        pprint(self.people)


class PersonInputTCPStream(PeopleInputStream):

    def read(self):
        data = client()
        people = from_data(data)
        self.people.extend(people)

        pprint(self.people)
