import socket
import json

from airlines.aircrafts import AirlineCompany, CargoAircraft, PassengerAircraft

from pprint import pprint

def client(host="localhost", port=6789):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip_address = socket.gethostbyname(host)

        airline = AirlineCompany("Chuppet In has AirCompany")
        cargo_aircraft = CargoAircraft("Avião de galinha", 5000, 2000, 10000)
        passenger_aircraft = PassengerAircraft("Boing 777 ao infinito e além", 250, 1500, 200)
        
        print("Sending data to server...")
        airline.add_aircrafts(cargo_aircraft, passenger_aircraft)

        client_socket.sendto(airline.serialize(), (ip_address, port))

        print("Waiting for response...")

        data, server_address = client_socket.recvfrom(1024)
        response = json.loads(data)  

        pprint(response)
        client_socket.close()

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    from airlines.utils import parse_args

    args = parse_args("UDP Client")
    client(args.host, args.port)