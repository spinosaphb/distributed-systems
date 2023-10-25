from dataclasses import dataclass
from typing import List
import pickle


@dataclass
class Aircraft:
    """
    Aircraft class

    :param model: Model of the aircraft
    :param capacity: Capacity of the aircraft
    :param range_: Range of the aircraft, this means how far the aircraft can fly
    """
    model: str
    capacity: int
    range_: int


    def __str__(self):
        return "\{"+f" Model: {self.model}\nCapacity: {self.capacity}\nRange: {self.range_}"+"/}"


class CargoAircraft(Aircraft):
    def __init__(self, model, capacity, range_, max_payload):
        super().__init__(model, capacity, range_)
        self.max_payload = max_payload
        self.autopilot_guided = True
    
    def __str__(self):
        return super().__str__() + f"\nMax Payload: {self.max_payload}"


class PassengerAircraft(Aircraft):
    def __init__(self, model, capacity, range_, passenger_count):
        super().__init__(model, capacity, range_)
        self.passenger_count = passenger_count
    
    def __str__(self):
        return super().__str__() + f"\nPassenger Count: {self.passenger_count}"


@dataclass
class AirlineCompany:
    name: str
    aircrafts: List[Aircraft] = None

    def __post_init__(self):
        if self.aircrafts is None:
            self.aircrafts = []

    def add_aircrafts(self, *aircrafts):

        for aircraft in aircrafts:
            self.aircrafts.append(aircraft)

    def __str__(self):
        aircrafts_str = ",\n".join([str(aircraft) for aircraft in self.aircrafts])
        return f"AirlineCompany\n\tName: {self.name}\n\tAircrafts: [\n{aircrafts_str}]"

    def serialize(self) -> bytes:
        return pickle.dumps(self)

    @staticmethod
    def deserialize(serialized) -> 'AirlineCompany':
        return pickle.loads(serialized)
        

