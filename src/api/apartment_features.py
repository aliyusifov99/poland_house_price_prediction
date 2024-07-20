from pydantic import BaseModel

class ApartmentFeatures(BaseModel):
    city: str
    type: str
    squareMeters: float
    rooms: int
    floor: int
    floorCount: int
    buildYear: float
    centreDistance: str
    poiCount: float
    schoolDistance: str
    clinicDistance: str
    postOfficeDistance: str
    kindergartenDistance: str
    restaurantDistance: str
    collegeDistance: str
    pharmacyDistance: str
    ownership: str
    buildingMaterial: str
    condition: str
    hasParkingSpace: str
    hasBalcony: str
    hasElevator: str
    hasSecurity: str
    hasStorageRoom: str
