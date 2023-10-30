from typing import List, BinaryIO
import pickle

class Person:
    def __init__(self, name: str, cpf: str, age: int):
        self.name = name
        self.cpf = cpf
        self.age = age

    def serialize(self):
        return pickle.dumps(self)
    
    @staticmethod
    def deserialize(data):
        return pickle.loads(data)
