from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId
from cbtw_process_api.models import Aircraft, AirlineCompany
from typing import List
from cbtw_process_api.config import (
    MONGODB_URL,
    MONGODB_DB,
    AIRCRAFTS_COLLECTION,
    AIRLINE_COMPANIES_COLLECTION,
    MAX_CONNECTIONS_COUNT,
    MIN_CONNECTIONS_COUNT,
)


class Repository:

    @classmethod
    def startup(cls) -> None:
        cls.client = AsyncIOMotorClient(
            MONGODB_URL,
            maxPoolSize=MAX_CONNECTIONS_COUNT,
            minPoolSize=MIN_CONNECTIONS_COUNT
        )
        cls.db = cls.client[MONGODB_DB]
        cls.aircrafts_collection = cls.db[AIRCRAFTS_COLLECTION]
        cls.airline_companies_collection = cls.db[AIRLINE_COMPANIES_COLLECTION]

    @classmethod
    def shutdown(cls) -> None:
        cls.client.close()

    async def create_aircraft(self, aircraft: Aircraft):
        aircraft_dict = aircraft.model_dump()
        result = await self.aircrafts_collection.insert_one(aircraft_dict)
        return result.inserted_id

    async def get_aircraft_by_id(self, aircraft_id: str) -> Aircraft | None:
        result = await self.aircrafts_collection.find_one({"_id": ObjectId(aircraft_id)}, {"_id": 0})
        return Aircraft(**result) if result else None

    async def get_all_aircrafts(self) -> List[Aircraft]:
        results = await self.aircrafts_collection.find({}, {"_id": 0}).to_list(None)
        return [Aircraft(**result) for result in results]

    async def update_aircraft(self, aircraft_id: str, new_aircraft: Aircraft):
        new_aircraft_dict = new_aircraft.model_dump()
        result = await self.aircrafts_collection.update_one(
            {"_id": ObjectId(aircraft_id)},
            {"$set": new_aircraft_dict}
        )
        if result.modified_count:
            return result.upserted_id

    async def delete_aircraft(self, aircraft_id: str):
        result = await self.aircrafts_collection.delete_one({"_id": ObjectId(aircraft_id)})
        return result.deleted_count
    
    async def create_airline_company(self, airline_company: AirlineCompany):
        airline_company_dict = airline_company.model_dump()
        result = await self.airline_companies_collection.insert_one(airline_company_dict)
        return result.inserted_id
    
    async def get_airline_company_by_id(self, airline_company_id: str) -> AirlineCompany | None:
        result = await self.airline_companies_collection.find_one(
            {"_id": ObjectId(airline_company_id)}, {"_id": 0}
        )
        return AirlineCompany(**result) if result else None
    
    async def get_all_airline_companies(self) -> List[AirlineCompany]:
        results = await self.airline_companies_collection.find({}, {"_id": 0}).to_list(None)
        return [AirlineCompany(**result) for result in results]
    
    async def update_airline_company(self, airline_company_id: str, new_airline_company: AirlineCompany):
        new_airline_company_dict = new_airline_company.model_dump()
        result = await self.airline_companies_collection.update_one(
            {"_id": ObjectId(airline_company_id)}, {"$set": new_airline_company_dict}
        )
        if result.modified_count:
            return result.upserted_id

    async def delete_airline_company(self, airline_company_id: str):
        result = await self.airline_companies_collection.delete_one(
            {"_id": ObjectId(airline_company_id)}
        )
        return result.deleted_count

