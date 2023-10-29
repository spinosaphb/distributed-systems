from PeopleOutputStream import PeopleOutputStream
from Person import Person
import socket
import struct

# Configure o servidor

# Crie um soquete do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associe o soquete ao endereço e porta
server_socket.bind(('0.0.0.0', 12345))

# Aguarde conexões
server_socket.listen(1)

print("Servidor aguardando conexões em 0.0.0.0:12345")

# Aceite uma conexão
client_socket, client_address = server_socket.accept()

print(f"Conexão estabelecida com {client_address}")

# Receba os dados do cliente e armazene-os em 'data'
data = b""
while True:
    chunk = client_socket.recv(1024)
    if not chunk:
        break
    data += chunk

# Agora 'data' contém os dados recebidos do cliente

people = []

while data:
    # Desserialize a pessoa
    name_size = struct.unpack('!I', data[:4])[0]
    data = data[4:]

    name = data[:name_size].decode('utf-8')
    data = data[name_size:]

    cpf = data[:9].decode('utf-8')
    data = data[9:]

    age = struct.unpack('!H', data[:2])[0]
    data = data[2:]

    person = Person(name, cpf, age)
    people.append(person)

# Agora 'people' contém as instâncias da classe Person desserializadas

# Imprima as informações das pessoas recebidas
for person in people:
    print(f"Nome: {person.name}, CPF: {person.cpf}, Idade: {person.age}")

# Feche os soquetes
client_socket.close()
server_socket.close()
