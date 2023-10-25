import socket
import random
import time
import sys

LOSS_RATE = 0.3
AVERAGE_DELAY = 0.1  # seconds

def print_data(data, address):
    print(f"Received from {address[0]}:{address[1]}: {data.decode()}")

def main():
    if len(sys.argv) != 2:
        print("Required arguments: port")
        return
    
    port = int(sys.argv[1])
    
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', port))
    
    while True:
        data, address = server_socket.recvfrom(1024)
        
        # Simulate packet loss
        if random.random() < LOSS_RATE:
            print("Reply not sent.")
            continue
        
        # Simulate network delay
        time.sleep(random.uniform(0, 2 * AVERAGE_DELAY))
        
        # Send the reply back to the client
        server_socket.sendto(data, address)
        print("Reply sent.")
        print_data(data, address)

if __name__ == "__main__":
    main()
