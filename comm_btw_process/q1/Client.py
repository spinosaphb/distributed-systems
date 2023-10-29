from Person import Person
from PeopleOutputStream import PeopleOutputStream

# Crie instâncias da classe Person
person1 = Person("Alice", "123456789", 30)
person2 = Person("Bob", "987654321", 25)

# Adicione as pessoas a uma lista
people = [person1, person2]

# Use PeopleOutputStream para enviar os dados
output_stream_stdout = PeopleOutputStream(people, open(1, 'wb'))  # Para a saída padrão
output_stream_stdout.send()

# Ou use para um arquivo
with open('people.bin', 'wb') as file_output_stream:
    output_stream_file = PeopleOutputStream(people, file_output_stream)
    output_stream_file.send()

# Ou use para um servidor remoto
import socket
import io

def send_data_to_remote_server(people_data: bytes):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('server_address', 12345))  # Substitua 'server_address' e 12345 pelo endereço e porta reais
        s.sendall(people_data)

output_stream_remote = PeopleOutputStream(people, io.BytesIO())
people_data = output_stream_remote.send()
send_data_to_remote_server(people_data)
