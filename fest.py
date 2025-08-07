import io
from pypdf import PdfReader, PdfWriter

from models import Festanmalan, Person


FA_NAME_FIELD = "Namn"
FA_PHONE_FIELD = "Mobiltelefonnummer"

CHAPTER_FIELD = "Sektion"

SA_NAME_FIELD = "Namn_2"
SA_PHONE_FIELD = "Mobiltelefonnummer_2"

BA_NAME_FIELD = "Namn_3"
BA_PHONE_FIELD = "Mobiltelefonnummer_3"

UL_NAME_FIELD = "Namn_4"
UL_PHONE_FIELD = "Mobiltelefonnummer_4"

CHAPTER_HALL_NAME_FIELD = "Namn_5"
CHAPTER_HALL_PHONE_FIELD = "Mobiltelefonnummer_5"

EVENT_DATE_FIELD = "Datum sammankomst"
EVENT_TIME_FIELD = "Starttid"
EVENT_LOCATION_FIELD = "Lokal"

EVENT_TYPE_FIELD = "Typ av sammankomst"

ALCOHOL_FIELD = "undefined_8"
PERMANENT_SERVING_FIELD = "undefined_10"

PERSON_COUNT_FIELD = "Antal personer"
ADDRESS_FIELD = "Adress"


def generate_pdf(anmalan: Festanmalan):
    reader = PdfReader("static/festanmalan.pdf")
    # Create a new PdfWriter instance for each call to ensure independence.
    writer = PdfWriter()
    # Append pages from the global reader. This is generally safe as PdfReader
    # is mostly read-only after initialization, and append copies page data.
    writer.append(reader)
    writer.update_page_form_field_values(
        writer.pages[0],
        {
            CHAPTER_FIELD: anmalan.chapter,
            FA_NAME_FIELD: anmalan.name,
            FA_PHONE_FIELD: anmalan.phone,
            # Adding other fields with default values for a more complete PDF
            SA_NAME_FIELD: anmalan.sa.name,
            SA_PHONE_FIELD: anmalan.sa.phone,
            BA_NAME_FIELD: anmalan.ba.name,
            BA_PHONE_FIELD: anmalan.ba.phone,
            UL_NAME_FIELD: anmalan.ul.name,
            UL_PHONE_FIELD: anmalan.ul.phone,
            CHAPTER_HALL_NAME_FIELD: anmalan.chapter_hall.name,
            CHAPTER_HALL_PHONE_FIELD: anmalan.chapter_hall.phone,
            EVENT_DATE_FIELD: anmalan.date,
            EVENT_TIME_FIELD: anmalan.time,
            EVENT_LOCATION_FIELD: anmalan.location,
            EVENT_TYPE_FIELD: anmalan.event_type,
            ALCOHOL_FIELD: (
                "/On" if anmalan.alcohol else "/Off"
            ),  # Checkboxes typically use /On or /Yes
            PERMANENT_SERVING_FIELD: "/On" if anmalan.permanent_serving else "/Off",
            PERSON_COUNT_FIELD: anmalan.person_count,
            ADDRESS_FIELD: anmalan.address,
        },
        auto_regenerate=False,
    )
    # Return the pdf as an in-memory stream
    pdf_buffer = io.BytesIO()
    writer.write(pdf_buffer)
    pdf_buffer.seek(0)  # Rewind the buffer to the beginning for reading
    return pdf_buffer
