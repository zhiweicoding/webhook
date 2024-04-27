from fastapi import APIRouter, Request
from pydantic import BaseModel

router = APIRouter()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


@router.post("/init/")
async def init(request: Request):
    # Parse the incoming JSON data
    data = await request.json()

    # You can process the data here
    print(data)

    # Return a response
    return {"message": "Data received successfully", "data": data}
