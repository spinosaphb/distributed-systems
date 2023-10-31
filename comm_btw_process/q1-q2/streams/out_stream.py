import io
from typing import List

from dataclasses import dataclass
from person import Person
from functools import reduce
from client import client

@dataclass
class PeopleOutputStream(io.IOBase):    
    people: List[Person]

    @property
    def size(self):
        return len(self.people)

    @property
    def data(self):
        data = f"{self.size}\n"
        data += reduce(lambda x, y: x + "\n" + y, map(str, self.people))
        return data

    def write(self):
        pass


class PersonOutputPrintStream(PeopleOutputStream):

    def write(self):
        print(self.data)


class PersonOutputFileStream(PeopleOutputStream):
    def write(self):
        with open("resources/people.txt", "w") as f:
            f.write(self.data)


class PersonOutputTCPStream(PeopleOutputStream):
    def write(self):
        client(self.data)