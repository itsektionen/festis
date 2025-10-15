from fastapi.responses import StreamingResponse
from fastapi.routing import APIRouter

from .models import Festanmalan

from .fest import generate_pdf


v1_router = APIRouter(prefix="/v1")


@v1_router.post(
    "/generate",
    name="Generate festanmälan",
    description="This endpoint generates a festanmälan .pdf with the data provided",
    response_description="The generated festanmälan .pdf",
    response_class=StreamingResponse,
)
async def generate_festanmalan(anmalan: Festanmalan):
    pdf = generate_pdf(anmalan)
    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={anmalan.date}.pdf"},
    )
