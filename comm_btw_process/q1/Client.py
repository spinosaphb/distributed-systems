from Person import Person
from PeopleOutputStream import PeopleOutputStream
import socket
import pickle
import io

# Crie instâncias da classe Person
person1 = Person("Alice", "123456789", 30)
person2 = Person("Bob", "987654321", 25)

# Adicione as pessoas a uma lista
people = [person1, person2]

# Serializar a lista de pessoas usando pickle
serialized_people = pickle.dumps(people)
print(">>>>",serialized_people,"\n")
# Ou use para um arquivo
with open('people.bin', 'wb') as file_output_stream:
    # Use o PeopleOutputStream para enviar os dados
    output_stream_file = PeopleOutputStream(serialized_people, file_output_stream)
    output_stream_file.send()

# Ou use para um servidor remoto
host = '192.168.1.2'
port = 12345

def send_data_to_remote_server(people_data: bytes):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(people_data)

# Use o PeopleOutputStream para enviar os dados para o servidor remoto
output_stream_remote = PeopleOutputStream(serialized_people, io.BytesIO())
people_data = output_stream_remote.send()
send_data_to_remote_server(people_data)
