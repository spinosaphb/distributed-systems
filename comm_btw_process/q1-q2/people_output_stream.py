import pickle
from person import Person
from typing import List, BinaryIO


class PeopleOutputStream:
    def __init__(self, people: List[Person], output_stream: BinaryIO):
        self.people = people
        self.output_stream = output_stream

    def send(self):
        serialized_people = pickle.dumps(self.people)
        
        self.output_stream.write(serialized_people)