from fastapi import FastAPI, Depends
from app.auth import verify_api_key
from app.routes.api import router as api_router
from fastapi.openapi.utils import get_openapi
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()

app.include_router(
    api_router,
    dependencies= [Depends(verify_api_key)]
)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Report Generator API",
        version="1.0.0",
        description="API with x-api-key header auth",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "APIKeyHeader": {
            "type": "apiKey",
            "in": "header",
            "name": "x-api-key"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"APIKeyHeader": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

logging.info("Files uploaded successfuly")
logging.info("Report generated successfully")