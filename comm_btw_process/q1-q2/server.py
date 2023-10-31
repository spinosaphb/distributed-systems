import socket

def server(port=6789):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_port = port
        server_socket.bind(('', server_port))

        while True:
            print("Running server...")
            
            data, client_address = server_socket.recvfrom(1024)
            phrase = data.decode('utf-8')
            client_ip, client_port = client_address
            
            print("Received connection from client with IP:", client_ip, "and port:", client_port)
            print("Phrase received:\n", phrase)
            
            phrase_in_uppercase = phrase.upper()
            print("custom phrase:\n", phrase_in_uppercase)

            data_to_send = phrase_in_uppercase.encode('utf-8')
            server_socket.sendto(data_to_send, client_address)
    except Exception as e:
        print("Error:", str(e))
    finally:
        server_socket.close()

if __name__ == "__main__":
    server()
