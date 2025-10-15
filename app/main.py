from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from scalar_fastapi import get_scalar_api_reference, Theme


from app.fest import generate_pdf
from app.models import Festanmalan

app = FastAPI(
    title="Festis",
    description="API for generating festanmälan .pdf's",
    docs_url=None,
    openapi_url="/openapi.json",
)

app.mount("/img", StaticFiles(directory="static/img"), name="img")


@app.get("/", include_in_schema=False)
def index():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
        theme=Theme.SATURN,
        scalar_favicon_url="img/favicon.png",
    )


@app.post(
    "/create",
    name="Create festanmälan",
    description="This endpoint creates a festanmälan .pdf with the data provided",
)
def festanmalan(anmalan: Festanmalan):
    pdf = generate_pdf(anmalan)
    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={anmalan.date}.pdf"},
    )
