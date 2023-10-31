import socket
from streams.utils import from_data
from pprint import pprint

def server(port=6789):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_port = port
        server_socket.bind(('', server_port))

        while True:
            print("Running server...")
            
            data, client_address = server_socket.recvfrom(1024)
            people_info = data.decode('utf-8')
            client_ip, client_port = client_address

            people = from_data(people_info)


            print("Received connection from client with IP:", client_ip, "and port:", client_port)
            print("Received:\n")
            pprint(people)

            phrase_in_uppercase = people_info.upper()
            print("custom phrase:\n", phrase_in_uppercase)

            data_to_send = phrase_in_uppercase.encode('utf-8')
            server_socket.sendto(data_to_send, client_address)

    except Exception as e:
        print("Error:", str(e))
    finally:
        server_socket.close()

if __name__ == "__main__":
    server()
