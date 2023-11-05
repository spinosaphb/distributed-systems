import socket


def vote(candidate_name: str, server_address):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(server_address)

    client.send(candidate_name.encode())
    response = client.recv(1024).decode()

    print(response)

    client.close()


if __name__ == '__main__':
    server_address = ('localhost', 8080)
    while True:
        candidate = input("Enter the candidate's name or 'exit' to end")
        if candidate.lower() == 'exit':
            break
        vote(candidate, server_address)
