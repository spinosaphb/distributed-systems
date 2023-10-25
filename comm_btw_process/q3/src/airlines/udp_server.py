import socket
import pickle
import json

from airlines.aircrafts import AirlineCompany


def make_response(airline: AirlineCompany):
    response = {
        "content": {
            "name": airline.name,
            "aircrafts": [str(aircraft) for aircraft in airline.aircrafts]
        },
        "status": "success"
    }
    return json.dumps(response).encode('utf-8')


def server(port=6789):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_port = port
        server_socket.bind(('', server_port))

        while True:
            data, client_address = server_socket.recvfrom(4096)
            received_obj = AirlineCompany.deserialize(data)
            client_ip, client_port = client_address

            print("Received connection from client with IP:", client_ip, "and port:", client_port)
            
            if isinstance(received_obj, AirlineCompany):
                print(f"Received data for Airline Company: [{str(received_obj)}]")
            else:
                print("Received unknown data")

            server_socket.sendto(make_response(received_obj), client_address)

    except Exception as e:
        print("Error:", str(e))
    finally:
        server_socket.close()


if __name__ == "__main__":
    from airlines.utils import parse_args

    args = parse_args("UDP Server")
    server(args.port)