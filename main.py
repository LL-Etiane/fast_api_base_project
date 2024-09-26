from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.openapi.utils import get_openapi
from app.routes.api import router as api_router
from middlewares.main import register_middlewares

app = FastAPI(redoc_url="/redoc", docs_url="/docs")

openapi_schema = get_openapi(
    title="FastApi Base API",
    version="1",
    description="Base project structure for my fastapi",
    routes=api_router.routes
)

openapi_schema["info"]["x-logo"] = {
    "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png",
    "altText": "fastapi Logo",
    "style": "padding: 10px; max-height: 50px; max-width: 50px;"
}

app.openapi_schema = openapi_schema

register_middlewares(app)

app.include_router(api_router)

@app.get("/")
async def redoc():
     # Redirect to redoc
    return RedirectResponse(url="/redoc")

