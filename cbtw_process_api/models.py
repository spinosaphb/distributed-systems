from pydantic import BaseModel
from typing import List, Optional

class Aircraft(BaseModel):
    """
    Aircraft class

    :param model: Model of the aircraft
    :param capacity: Capacity of the aircraft
    :param range_: Range of the aircraft, this means how far the aircraft can fly
    """
    model: str
    capacity: int
    range_: int


class CargoAircraft(Aircraft):
    """
    CargoAircraft class

    :param max_payload: Maximum payload of the aircraft
    :param autopilot_guided: Is the aircraft autopilot guided
    """
    max_payload: int
    autopilot_guided: bool = True


class PassengerAircraft(Aircraft):
    """
    PassengerAircraft class

    :param passenger_count: Passenger count of the aircraft
    """
    passenger_count: int


class AirlineCompany(BaseModel):
    """
    AirlineCompany class

    :param name: Name of the airline company
    """
    name: str
    aircrafts: Optional[List[Aircraft]] = None

    def __post_init__(self):
        if self.aircrafts is None:
            self.aircrafts = []

    def add_aircrafts(self, *aircrafts):

        for aircraft in aircrafts:
            self.aircrafts.append(aircraft)
