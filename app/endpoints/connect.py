
from fastapi import APIRouter

router = APIRouter()

@router.get("/connect")
async def get_connections():
      return {"Hello": "I'm Flora"}