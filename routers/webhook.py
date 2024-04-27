from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/init/")
async def init(request: Request):
    # Parse the incoming JSON data
    data = await request.json()

    # You can process the data here
    print(data)

    # Return a response
    return {"message": "Data received successfully", "data": data}
