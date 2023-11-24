from fastapi.routing import APIRouter, JSONResponse
from models import (
    Aircraft,
    CargoAircraft,
    PassengerAircraft,
    AirlineCompany
)
from db import Repository
from typing import List


router = APIRouter()
repository = Repository()

# Aircrafts Routes
@router.get("/aircrafts", tags=["Aircrafts"])
async def get_aircrafts()-> List[Aircraft]:
    """
    Get all aircrafts
    """
    result = await repository.get_all_aircrafts()
    return result


@router.get("/aircrafts/{aircraft_id}", tags=["Aircrafts"])
async def get_aircraft(aircraft_id: str) -> Aircraft:
    """
    Get aircraft by id
    """
    result = await repository.get_aircraft_by_id(aircraft_id)
    return result


async def _add_aircraft(aircraft: Aircraft) -> JSONResponse:
    result = await repository.create_aircraft(aircraft)
    return JSONResponse(
        status_code=201,
        content={"message": f"{aircraft.__class__.__name__} created with id: {result}"}
    )


@router.post("/aircrafts", tags=["Aircrafts"])
async def add_aircraft(aircraft: Aircraft) -> JSONResponse:
    """
    Add aircraft
    """
    return await _add_aircraft(aircraft)


@router.post("/aircrafts/cargo", tags=["Aircrafts"])
async def add_cargo_aircraft(cargo_aircraft: CargoAircraft) -> JSONResponse:
    """
    Add cargo aircraft
    """
    return await _add_aircraft(cargo_aircraft)


@router.post("/aircrafts/passenger", tags=["Aircrafts"])
async def add_passenger_aircraft(passenger_aircraft: PassengerAircraft) -> JSONResponse:
    """
    Add passenger aircraft
    """
    return await _add_aircraft(passenger_aircraft)


@router.put("/aircrafts/{aircraft_id}", tags=["Aircrafts"])
async def update_aircraft(aircraft_id: int, aircraft: Aircraft):
    """
    Update aircraft
    """
    upserted_id = await repository.update_aircraft(aircraft_id, aircraft)
    
    if upserted_id is None:
        return JSONResponse(
            status_code=404,
            content={"message": f"Document with id: {aircraft_id} not found"}
        )
    
    return JSONResponse(
        status_code=200,
        content={"message": f"Document with id: {aircraft_id} updated"}
    )


@router.delete("/aircrafts/{aircraft_id}", tags=["Aircrafts"])
async def delete_aircraft(aircraft_id: int):
    """
    Delete aircraft
    """
    deleted_count = await repository.delete_aircraft(aircraft_id)
    
    if deleted_count == 0:
        return JSONResponse(
            status_code=404,
            content={"message": f"Document with id: {aircraft_id} not found"}
        )
    
    return JSONResponse(
        status_code=200,
        content={"message": f"Document with id: {aircraft_id} deleted"}
    )


#Airline Companies Routes
@router.get("/airline-companies", tags=["Airline Companies"])
async def get_airline_companies():
    """
    Get all airline companies
    """
    result = await repository.get_all_airline_companies()
    return result
    


@router.get("/airline-companies/{airline_company_id}", tags=["Airline Companies"])
async def get_airline_company(airline_company_id: int):
    """
    Get airline company by id
    """
    result = await repository.get_airline_company_by_id(airline_company_id)
    return result


@router.post("/airline-companies", tags=["Airline Companies"])
async def add_airline_company(airline_company: AirlineCompany):
    """
    Add airline company
    """
    result = await repository.create_airline_company(airline_company)
    return JSONResponse(
        status_code=201,
        content={"message": f"{airline_company.__class__.__name__} created with id: {result}"}
    )


@router.put("/airline-companies/{airline_company_id}", tags=["Airline Companies"])
async def update_airline_company(
    airline_company_id: int,
    airline_company: AirlineCompany
):
    """
    Update airline company
    """
    upserted_id = await repository.update_airline_company(airline_company_id, airline_company)
    
    if upserted_id is None:
        return JSONResponse(
            status_code=404,
            content={"message": f"Document with id: {airline_company_id} not found"}
        )
    
    return JSONResponse(
        status_code=200,
        content={"message": f"Document with id: {airline_company_id} updated"}
    )


@router.delete("/airline-companies/{airline_company_id}", tags=["Airline Companies"])
async def delete_airline_company(airline_company_id: int):
    """
    Delete airline company
    """
    deleted_count = await repository.delete_airline_company(airline_company_id)
    
    if deleted_count == 0:
        return JSONResponse(
            status_code=404,
            content={"message": f"Document with id: {airline_company_id} not found"}
        )
    
    return JSONResponse(
        status_code=200,
        content={"message": f"Document with id: {airline_company_id} deleted"}
    )