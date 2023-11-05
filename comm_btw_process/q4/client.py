import socket
from typing import Optional


class Client:

    client: Optional[socket.socket] = None
    active: bool = True

    def __init__(self, server_address: tuple[str, int]) -> None:
        self.server_address = server_address

    def startup(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.server_address)

    def shutdown(self):
        self.client.close()

    def get_question(self):
        question = self.client.recv(1024).decode()
        return question

    def send_answer(self):
        answer = input()
        self.client.send(answer.encode())


if __name__ == '__main__':
    host = '192.168.1.2'
    port = 8080
    server_address = (host, port)
    client = Client(server_address)
    client.startup()
    while client.active:
        message = client.get_question()
        print(message, " ")
        if(message):
            client.send_answer()
    client.shutdown()
