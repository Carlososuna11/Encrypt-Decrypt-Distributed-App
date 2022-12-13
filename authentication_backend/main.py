import controllers  # noqa: F401
import os
from ray import serve
import ray
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

    # creates a fastAPI instance
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
        openapi_url="/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # adds CORS middleware
    app.add_middleware(
        CORSMiddleware,
        **settings.CORS_SETTINGS
    )

    # add here the routers...
    app.include_router(
        routers.authentication.router,
    )

    return app


# set the environment variable to the settings module
os.environ.setdefault('FASTAPI_CONFIG', 'core.settings')
app = get_application()

# create a Ray Serve deployment with the prefix /authentication


@serve.deployment(
    name="authentication-backend",
    route_prefix="/authentication"
)
# this class is needed to make Ray Serve work
@serve.ingress(app)
class FastAPIWrapper:
    pass


# set the working directory to the root of the project
runtime_env = {
    "working_dir": "/usr/src/app",
}

# start the Ray Serve instance
with ray.init(
        address=settings.RAY_ADDRESS,
        runtime_env=runtime_env,
        namespace=str(uuid.uuid4())
):
    # start the FastAPIWrapper deployment
    serve.start(
        detached=True,
        http_options={
            "host": "0.0.0.0",
            "port": 8000,
        }
    )
    # deploy the FastAPIWrapper
    FastAPIWrapper.deploy()
