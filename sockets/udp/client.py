import socket

def client(host="localhost", port=6789):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        server_host = host
        server_port = port
        
        IPAddress = socket.gethostbyname(server_host)
        print("local IP:", IPAddress)
        
        message = "distributed systems"
        print("original message:", message)
        
        client_socket.sendto(message.encode('utf-8'), (IPAddress, server_port))
        
        data, server_address = client_socket.recvfrom(1024)
        modified_message = data.decode('utf-8')
        
        print("from server:", modified_message)
        client_socket.close()
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    # --host localhost --port 6789
    client()
