import socket
import threading

def server(server_host= "localhost", server_port= 7896):
    server_host = server_host
    server_port = server_port
    
    try:
        print("Server started")
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.bind((server_host, server_port))
        listen_socket.listen(5)
        
        while True:
            client_socket, client_address = listen_socket.accept()
            print(client_address)
            print("connection established")
            connection = Connection(client_socket)
            connection.start()
    except Exception as e:
        print("Listen socket:", str(e))

class Connection(threading.Thread):
    def __init__(self, client_socket):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
    
    def run(self):
        try:
            data = self.client_socket.recv(1024).decode('utf-8')
            print(data)
            self.client_socket.send(data.upper().encode('utf-8'))
        except Exception as e:
            print("Error:", str(e))
        finally:
            self.client_socket.close()

if __name__ == "__main__":
    server()
