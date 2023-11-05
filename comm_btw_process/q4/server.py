import socket
import threading
from voting import VotingManager
from user import User


def handle_client(
    client_socket: socket.socket,
    addr,
    user: User,
    voting_manager: VotingManager
):
    print(f"Connection accepted from {addr[0]}:{addr[1]}")

    def get_answer(question: str) -> str:
        client_socket.send(question.encode())
        return client_socket.recv(1024).decode()

    if not voting_manager.active_voting:
        client_socket.send("Voting has already been closed.".encode())
        client_socket.close()
        return

    if user.is_admin():
        while True:
            client_socket.send("""Administrative options:
                (1) Add candidate
                (2) Remove candidate
                (3) Send note
                (4) Close
            """.encode())
            admin_option = client_socket.recv(1024).decode()

            match admin_option:
                case '1':
                    candidate_name = get_answer("Enter the candidate's name: ")
                    voting_manager.service.create_candidate(candidate_name)
                    print(f"Candidate {candidate_name} created successfully.")
                case '2':
                    candidate_id = get_answer("Enter the candidate's id: ")
                    voting_manager.service.remove_candidate(candidate_id)
                    print(f"Candidate {candidate_id} removed successfully.")
                case '3':
                    note = get_answer("Enter the note: ")
                    client_socket.send(note.encode())
                    response = client_socket.recv(1024).decode()
                    print(response)
                case '4':
                    break
    else:
        candidates = voting_manager.service.get_candidates()
        while True:
            candidate = input("Enter the candidate's name or 'exit' to end: ")
            if candidate.lower() == 'exit':
                break
            if candidate in candidates:
                client_socket.send(candidate.encode())
                response = client_socket.recv(1024).decode()
                print(response)
            else:
                print("Invalid candidate.")

    client_socket.close()


def start_server(voting_manager: VotingManager):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8080))
    server.listen(5)
    print("Voting server started...")

    # Start the voting timer
    voting_timer_thread = threading.Thread(target=voting_manager.close_voting)
    voting_timer_thread.start()

    while True:
        client_socket, addr = server.accept()
        print(f"Connection accepted from {addr[0]}:{addr[1]}")

        client_socket.send("Enter your username:".encode())
        username = client_socket.recv(1024).decode()

        client_socket.send("Enter your password:".encode())
        password = client_socket.recv(1024).decode()

        user = voting_manager.authenticate_user(username, password)
        if user:
            client_socket.send(f"Login successful as {user.role}.\n".encode())
            client_handler = threading.Thread(
                target=handle_client,
                args=(client_socket, addr, user, voting_manager)
            )
            client_handler.start()
        else:
            client_socket.send(
                "Login failed. Incorrect username or password.\n".encode()
            )


if __name__ == "__main__":
    voting_manager = VotingManager()
    voting_manager.startup()
    start_server(voting_manager)