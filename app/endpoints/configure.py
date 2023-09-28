
from fastapi import (
    APIRouter,
    Request,
    Response,
    Depends
)
from app.schemas.models import ConfigSchema
from app.dependencies import get_db

router = APIRouter()


@router.post("/configure")
async def set_configuration(request: Request, payload: ConfigSchema, session=Depends(get_db)):

    configure_repo = request.app.repositories.get('configure')(session)
    configure = configure_repo.add(payload)
    return payload.dict()
