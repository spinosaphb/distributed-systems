import json
from user import User
from db import Service
from candidate import Candidate
from typing import Iterable
from functools import reduce
import time


class VotingManager:
    def __init__(self):
        self._service = None
        self.active_voting = True

    def close_voting(self):
        self.startup()
        time_limit = 30  # For example, 60 seconds
        time.sleep(time_limit)
        print("Voting has been closed.")
        winner, percentages = \
            self.calculate_winner(self.service.get_candidates())
        print(f"Winner: {winner.name}. Percentages: {percentages}")
        self.active_voting = False

    def startup(self):
        self.service = Service()
        self.service.startup()

    def shutdown(self):
        self.service.shutdown()

    def populate_candidates(self):
        candidates = json.load(open('resources/candidates.json'))
        for candidate in candidates["candidates"]:
            self.service.create_candidate(candidate["name"])
        return self.service.get_candidates()

    def calculate_winner(self, candidates: Iterable[Candidate]):
        total_votes = \
            reduce(lambda x, y: x + y, map(lambda c: c.nvotes, candidates))
        winner = max(candidates, key=lambda c: c.nvotes)
        percentages = {
            candidate.name: candidate.nvotes / total_votes * 100
            for candidate in candidates
        }
        return winner, percentages

    @staticmethod
    def authenticate_user(username, password):
        with open('resources/users.json') as users_file:
            users_data = json.load(users_file)
            users = users_data.get("users", [])
            for user_info in users:
                user_info_username = user_info["username"]
                user_info_password = user_info["password"]
                if user_info_username == username and \
                        user_info_password == password:
                    return User(username, password, user_info["role"])
        return None
