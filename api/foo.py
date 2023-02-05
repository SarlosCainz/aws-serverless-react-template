from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv

router = InferringRouter()


@cbv(router)
class FooCDV:
    @router.get("/")
    async def get_foo(self):
        return "success"
