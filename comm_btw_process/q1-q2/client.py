import socket

def client(data, host="localhost", port=6789):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        server_host = host
        server_port = port
        
        IPAddress = socket.gethostbyname(server_host)
        print("local IP:", IPAddress)
        
        print("original message:\n", data)
        
        client_socket.sendto(data.encode('utf-8'), (IPAddress, server_port))
        
        data, server_address = client_socket.recvfrom(1024)
        modified_message = data.decode('utf-8')
        
        print("from server:\n", modified_message)
        client_socket.close()
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    client()
