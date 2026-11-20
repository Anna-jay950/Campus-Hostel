from fastapi import FastAPI
from pydantic import BaseModel

class Hostel(BaseModel):
    name: str
    location: str
    price: float
    facilities: list[str]

app = FastAPI()

hostels = [
    {
        "id": 1,
        "name": "Royal Gardens Hostel",
        "location": "Ayeduase",
        "price": 4500,
        "facilities": ["Wi-Fi", "Water", "Security"]
    },
    {
        "id": 2,
        "name": "Campus View Hostel",
        "location": "Kotei",
        "price": 3800,
        "facilities": ["Water", "Parking", "Security"]
    },
    {
        "id": 3,
        "name": "Golden Gate Hostel",
        "location": "Ayeduase",
        "price": 5000,
        "facilities": ["Wi-Fi", "Laundry", "Security"]
    },
    {
        "id": 4,
        "name": "Unity Residence",
        "location": "Bomso",
        "price": 3500,
        "facilities": ["Water", "Kitchen", "Wi-Fi"]
    },
    {
        "id": 5,
        "name": "Green Valley Hostel",
        "location": "Kotei",
        "price": 4200,
        "facilities": ["Wi-Fi", "Water", "Parking"]
    }
]

@app.get("/")
def root():
  return {"message":  "Welcome to Campus Hostel Discovery API"}

@app.get("/hostels")
def get_hostels():
  return hostels

@app.get("/hostels/{hostel_id}")
def get_hostel(hostel_id: int):
    for hostel in hostels:
        if hostel["id"] == hostel_id:
            return hostel

    return {"error": "Hostel not found"}


@app.get("/search")
def search_hostels(location: str):
    results = []

    for hostel in hostels:
        if hostel["location"].lower() == location.lower():
            results.append(hostel)

    return results


@app.post("/hostels")
def create_hostel(hostel: Hostel):
    new_hostel = {
        "id": len(hostels) + 1,
        **hostel.model_dump()
    }

    hostels.append(new_hostel)

    return new_hostel
