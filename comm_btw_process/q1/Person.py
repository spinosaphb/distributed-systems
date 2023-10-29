import struct
from typing import List, BinaryIO

class Person:
    def __init__(self, name: str, cpf: str, age: int):
        self.name = name
        self.cpf = cpf
        self.age = age

    def serialize(self):
        name_bytes = self.name.encode('utf-8')
        name_size = len(name_bytes)
        cpf_bytes = self.cpf.encode('utf-8')
        age_bytes = struct.pack('!H', self.age)

        return struct.pack('!I', name_size) + name_bytes + cpf_bytes + age_bytes
    
    @classmethod
    def deserialize(cls, data):
        name_size = struct.unpack('!I', data[:4])[0]
        data = data[4:]

        name = data[:name_size].decode('utf-8')
        data = data[name_size:]

        cpf = data[:9].decode('utf-8')
        data = data[9:]
        age = struct.unpack('!H', data[:2])[0]
        return cls(name, cpf, age)
