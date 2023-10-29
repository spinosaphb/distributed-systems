import struct
from Person import Person
from typing import List, BinaryIO

class PeopleOutputStream:
    def __init__(self, peoples: List[Person], output_stream: BinaryIO):
        self.peoples = peoples
        self.output_stream = output_stream

    def send(self):
        # Enviar o número de pessoas
        num_people = len(self.peoples)
        self.output_stream.write(struct.pack('!I', num_people))

        for person in self.peoples:
            # enviar a pessoa serializada
            serialized_data = person.serialize()
            self.output_stream.write(serialized_data)
