from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from scalar_fastapi import get_scalar_api_reference, Theme

from app.v1.routers import v1_router

app = FastAPI(
    title="Festis",
    description="API for generating festanmälan .pdf's",
    docs_url=None,
    openapi_url="/openapi.json",
    version="0.1.0",
)

app.mount("/img", StaticFiles(directory="static/img"), name="img")
app.include_router(v1_router)


@app.get("/", include_in_schema=False)
def index():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
        theme=Theme.SATURN,
        scalar_favicon_url="img/favicon.png",
    )
