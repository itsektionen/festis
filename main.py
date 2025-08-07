from typing import Union

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import StreamingResponse
from scalar_fastapi import get_scalar_api_reference


from fest import generate_pdf
from models import Festanmalan

app = FastAPI(title="festing", docs_url=None, openapi_url=None)

@app.post("/create")
def festanmalan(anmalan: Festanmalan):
    print(anmalan)
    pdf = generate_pdf(anmalan)
    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={anmalan.name}.pdf"},
    )
