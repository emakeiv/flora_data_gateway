
from fastapi import APIRouter
from app.schemas.models import ConfigSchema

from sources import get_source
router = APIRouter()


@router.post("/scan")
async def get_devices(re: ConfigSchema):

    source = get_source(
        config=None,
        data_source=re.data_source,
        device_id=re.device_id,
        connect=re.auto_connect
    )

    device_id_list = source.list_available_devices()

    return {"Hello": device_id_list}
