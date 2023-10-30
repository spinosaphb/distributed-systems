import pickle
from Person import Person
from typing import List, BinaryIO

class PeopleOutputStream:
    def __init__(self, people: List[Person], output_stream: BinaryIO):
        self.people = people
        self.output_stream = output_stream

    def send(self):
        # Serializar a lista de pessoas usando pickle
        serialized_people = pickle.dumps(self.people)
        
        # Enviar a lista de pessoas serializada
        self.output_stream.write(serialized_people)