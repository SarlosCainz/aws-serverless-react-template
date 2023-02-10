from typing import List

from fastapi import Depends
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
import boto3

from api.config import settings
from api.models import Doc
import api.util
import api.auth


router = InferringRouter()
logger = api.util.get_logger()


@cbv(router)
class JwtAuthCDV:
    token: str = Depends(api.auth.get_valid_token)

    @router.get("/docs", response_model=List[Doc])
    async def api_list(self):
        result = []
        prefix = "docs/"
        for key, content in api.util.s3_objects(prefix):
            logger.debug(key)
            title = list(content["Body"].iter_lines())[0]
            last_update = content["LastModified"].astimezone(api.util.jst)
            doc = Doc(filename=key, content=title, last_update=last_update)
            result.append(doc)

        return result
