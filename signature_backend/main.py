import controllers  # noqa: F401
import os
import ray
from ray import serve
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from conf import settings
import routers
import uuid


def get_application() -> FastAPI:
    """
    Returns a FastAPI application.
    :return: FastAPI application.
    """

    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
        openapi_url="/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    app.add_middleware(
        CORSMiddleware,
        **settings.CORS_SETTINGS
    )

    # add here the routers...
    app.include_router(
        routers.signature.router,
    )
    return app


os.environ.setdefault('FASTAPI_CONFIG', 'core.settings')
app = get_application()


@serve.deployment(
    name="signature-backend",
    route_prefix="/signature"
)
@serve.ingress(app)
class FastAPIWrapper:
    pass


runtime_env = {
    "working_dir": "/usr/src/app",
}


with ray.init(
        address=settings.RAY_ADDRESS,
        runtime_env=runtime_env,
        namespace=str(uuid.uuid4())
):

    serve.start(
        detached=True,
        http_options={
            "host": "0.0.0.0",
            "port": 8000,
        }
    )
    FastAPIWrapper.deploy()
