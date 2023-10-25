import socket

def client(host="localhost", port=7896):
    # arguments supply message and hostname
    server_host = host
    server_port = port
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server_host, server_port))
        
        message = "sistemas_distribuidos"
        print("Sent: ", message)
        s.send(message.encode('utf-8'))

        data = s.recv(1024).decode('utf-8')
        print("Received: ", data)
    except ConnectionRefusedError:
        print("Connection refused.")
    except Exception as e:
        print("Error:", e)
    finally:
        s.close()

if __name__ == "__main__":
    from sockets.utils import parse_args

    args = parse_args("TCP Client")
    client(args.host, args.port)
