import socket
import threading
from voting import VotingManager
from user import User
from message import Message


def get_answer(client_socket: socket.socket, question: str) -> str:
    client_socket.send(Message(question).serialized)
    return client_socket.recv(1024).decode()

def send_message(client_socket: socket.socket, message: str) -> None:
    client_socket.send(Message(message, False).serialized)


def handle_client(
    client_socket: socket.socket,
    addr,
    user: User,
    voting_manager: VotingManager
):
    voting_manager.startup()
    send_message(client_socket, f"Login successful as {user.role}.\n")
    print(f"[handle_client]Connection accepted from {addr[0]}:{addr[1]}")

    if not voting_manager.active_voting:
        send_message(client_socket, "Voting has already been closed.")
        client_socket.close()
        return

    if user.is_admin():
        while True:
            admin_option =get_answer(client_socket,"""Administrative options:
                (1) Add candidate
                (2) Remove candidate
                (3) Send note
                (4) Close
            """.encode())

            match admin_option:
                case '1':
                    candidate_name = get_answer(client_socket, "Enter the candidate's name: ")
                    voting_manager.service.create_candidate(candidate_name)
                    print(f"Candidate {candidate_name} created successfully.")
                case '2':
                    candidate_id = get_answer(client_socket, "Enter the candidate's id: ")
                    voting_manager.service.remove_candidate(candidate_id)
                    print(f"Candidate {candidate_id} removed successfully.")
                case '3':
                    note = get_answer(client_socket, "Enter the note: ")
                    print(note)
                    send_message(client_socket, note)
                case '4':
                    break
    else:
        candidates = voting_manager.service.get_candidates()
        while True:
            candidate = get_answer(client_socket, 
                "Enter the candidate's name or 'exit' to end: "
            )
            if candidate.lower() == 'exit':
                break
            if candidate in candidates:
                response = get_answer(client_socket, candidate)
                print(response)
            else:
                print("Invalid candidate.")

    client_socket.close()


def start_server(voting_manager: VotingManager):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '192.168.1.2'
    port = 8080
    server.bind((host, port))
    server.listen(5)
    print("Voting server started...")

    # Start the voting timer
    voting_timer_thread = threading.Thread(target=voting_manager.close_voting)
    voting_timer_thread.start()

    while True:
        client_socket, addr = server.accept()
        print(f"Connection accepted from {addr[0]}:{addr[1]}")

        username = get_answer(client_socket,"Enter your username:")
        password = get_answer(client_socket, "Enter your password:")

        user = voting_manager.authenticate_user(username, password)
        if user:
            client_handler = threading.Thread(
                target=handle_client,
                args=(client_socket, addr, user, voting_manager)
            )
            client_handler.start()
        else:
            send_message(client_socket,"Login failed. Incorrect username or password.")


if __name__ == "__main__":
    voting_manager = VotingManager()
    start_server(voting_manager)