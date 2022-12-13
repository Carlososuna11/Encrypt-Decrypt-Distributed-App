from fastapi import (APIRouter)
from controllers import (
    authenticate,
    verify,
)
router = APIRouter(
    tags=["Authentication Server"],
)


router.add_api_route(
    path="/authenticate",
    endpoint=authenticate,
    methods=["POST"],
    include_in_schema=False,
)

router.add_api_route(
    path="/authenticate/",
    endpoint=authenticate,
    methods=["POST"],
)

router.add_api_route(
    path="/verify",
    endpoint=verify,
    methods=["POST"],
    include_in_schema=False,
)

router.add_api_route(
    path="/verify/",
    endpoint=verify,
    methods=["POST"],
)
