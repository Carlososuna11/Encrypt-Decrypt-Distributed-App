from fastapi import (APIRouter)
from controllers import (
    signature
)

# create a router for the signature server
router = APIRouter(
    tags=["Signature Server"],
)

# add the endpoint to the router
router.add_api_route(
    path="/",
    endpoint=signature,
    methods=["POST"],
)
