from fastapi import (APIRouter)
from controllers import (
    signature
)
router = APIRouter(
    tags=["Signature Server"],
)

router.add_api_route(
    path="/",
    endpoint=signature,
    methods=["POST"],
)
