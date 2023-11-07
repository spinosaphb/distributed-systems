#server.py
import socket
import threading
from voting import VotingManager
from user import User
from message import Message
from pprint import pprint


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
        alive = True
        while alive:
            admin_option =get_answer(client_socket,"""Administrative options:
                (1) Add candidate
                (2) Remove candidate
                (3) Send note
                (4) Candidates status
                (5) Close
            """)

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
                    candidates = voting_manager.service.get_candidates()
                    candidates_str = [f"Id: {candidate.candidate_id} - Name: {candidate.name} => Score: {candidate.nvotes}" for candidate in candidates]
                    send_message(client_socket, 'Candidates Scoring:\n' + '\n'.join(candidates_str)+"\n------------------")
                case '5':
                    alive = False
                    break
    else:
        while True:
            candidates = voting_manager.service.get_candidates()
            candidates_map = {c.candidate_id: c.name for c in candidates}
            candidates_str = [f"Id: {candidate.candidate_id} - Name: {candidate.name}" for candidate in candidates]
            send_message(client_socket, 'Candidates:\n' + '\n'.join(candidates_str)+"\n------------------")

            candidate_id = int(get_answer(client_socket, 
                "Enter the candidate's id or '0' to end: "
            ))
            if candidate_id == 0:
                break
            if candidate_id in candidates_map:
                voting_manager.service.update_candidate(candidate_id)
                send_message(client_socket, f"Your vote in {candidates_map[candidate_id]} was registered!\n\nWaiting the result...")
                while VotingManager.active_voting: pass
                break
            send_message(client_socket, "Invalid candidate.")

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
        while True:
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
                continue
            break
            


if __name__ == "__main__":
    try:
        voting_manager = VotingManager()
        start_server(voting_manager)
    except Exception as e:
        pprint(e)
        exit()