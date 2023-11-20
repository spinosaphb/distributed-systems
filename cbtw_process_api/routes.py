from fastapi.routing import APIRouter
from cbtw_process_api.models import (
    Aircraft,
    CargoAircraft,
    PassengerAircraft,
    AirlineCompany
)

router = APIRouter()

# Aircrafts Routes
@router.get("/aircrafts", tags=["Aircrafts"])
def get_aircrafts():
    """
    Get all aircrafts
    """
    pass


@router.get("/aircrafts/{aircraft_id}", tags=["Aircrafts"])
def get_aircraft(aircraft_id: int):
    """
    Get aircraft by id
    """
    pass


@router.post("/aircrafts", tags=["Aircrafts"])
def add_aircraft(aircraft: Aircraft):
    """
    Add aircraft
    """
    pass


@router.post("/aircrafts/cargo", tags=["Aircrafts"])
def add_cargo_aircraft(cargo_aircraft: CargoAircraft):
    """
    Add cargo aircraft
    """
    pass


@router.post("/aircrafts/passenger", tags=["Aircrafts"])
def add_passenger_aircraft(passenger_aircraft: PassengerAircraft):
    """
    Add passenger aircraft
    """
    pass


@router.put("/aircrafts/{aircraft_id}", tags=["Aircrafts"])
def update_aircraft(aircraft_id: int, aircraft: Aircraft):
    """
    Update aircraft
    """
    pass


@router.delete("/aircrafts/{aircraft_id}", tags=["Aircrafts"])
def delete_aircraft(aircraft_id: int):
    """
    Delete aircraft
    """
    pass


#Airline Companies Routes
@router.get("/airline-companies", tags=["Airline Companies"])
def get_airline_companies():
    """
    Get all airline companies
    """
    pass


@router.get("/airline-companies/{airline_company_id}", tags=["Airline Companies"])
def get_airline_company(airline_company_id: int):
    """
    Get airline company by id
    """
    pass


@router.post("/airline-companies", tags=["Airline Companies"])
def add_airline_company(airline_company: AirlineCompany):
    """
    Add airline company
    """
    pass


@router.put("/airline-companies/{airline_company_id}", tags=["Airline Companies"])
def update_airline_company(
    airline_company_id: int,
    airline_company: AirlineCompany
):
    """
    Update airline company
    """
    pass


@router.delete("/airline-companies/{airline_company_id}", tags=["Airline Companies"])
def delete_airline_company(airline_company_id: int):
    """
    Delete airline company
    """
    pass