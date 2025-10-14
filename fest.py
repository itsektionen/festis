import io
from pypdf import PdfReader, PdfWriter

from models import Festanmalan

# TODO: Implement chapters as enums
#
# A-Arkitektursektionen
# B- Kongliga Bergssektionen
# CL- Sektionen för Civilingenjör och Lärare
# D- Kongliga Datasektionen
# Dr- Doktorandsektionen
# E- Konglig Elektrosektionen
# F- Fysiksektionen
# I- Sektionen för Industriell ekonomi
# IN- Sektionen för Informations- och Nanoteknik
# IsB- Ingenjörssektionen Bygg
# IsF- Ingenjörsektionen Flemingsberg
# K- kongliga Kemisektionen
# M- Kungliga Maskinsektionen
# Media- Sektionen för Mediateknik
# MiT- Sektionen för Medicinsk Teknik
# OPEN- Öppen ingång
# P - Produktionssektionen
# S- Konglig Samhällsbyggnadssektion
# T- Flygsektionen
# W- Energi och Miljö

# TODO: Implement event types as enums
#
# Fest
# Filmkväll
# Gasque
# Grillfest
# LAN
# Middag
# Möte
# Pub
# Sillis
# Sittning
# Spelkväll
# Tentapub

# Sektion:
CHAPTER_FIELD = "Sektion"

# Festansvarig
FA_NAME_FIELD = "Namn"
FA_PHONE_FIELD = "Mobiltelefonnummer"

# Serveringsansvarig
SA_NAME_FIELD = "Namn_2"
SA_PHONE_FIELD = "Mobiltelefonnummer_2"

# Brandansvarig
BA_NAME_FIELD = "Namn_3"
BA_PHONE_FIELD = "Mobiltelefonnummer_3"

# Utrymningsledare:
UL_NAME_FIELD = "Namn_4"
UL_PHONE_FIELD = "Mobiltelefonnummer_4"

# Plats:
EVENT_LOCATION_FIELD = "Lokal"
ADDRESS_FIELD = "Adress"

# Sektionslokalsansvarig:
CHAPTER_HALL_NAME_FIELD = "Namn_5"
CHAPTER_HALL_PHONE_FIELD = "Mobiltelefonnummer_5"

# Typ av sammankomst:
EVENT_TYPE_FIELD = "Typ av sammankomst"
EVENT_DATE_FIELD = "Datum sammankomst"
EVENT_START_TIME_FIELD = "Starttid"
EVENT_END_TIME_FIELD = "Sluttid"
PERSON_COUNT_FIELD = "Antal personer"
GRILL_FIELD = "undefined_6"

# Alkoholservering:
# Servering av alkohol:
ALCOHOL_YES_FIELD = "undefined_8"
ALCOHOL_NO_FIELD = "undefined_9"
PERMANENT_SERVING_FIELD = "undefined_10"

# Serveringstillstånd:
TEMPORARY_PERMIT_FIELD = "undefined_11"
EXTENDED_GUESTS_FIELD = "undefined_12"
EXTENDED_AREA_FIELD = "undefined_13"


def generate_pdf(anmalan: Festanmalan):
    reader = PdfReader("static/festanmalan.pdf")

    writer = PdfWriter()

    writer.append(reader)
    writer.update_page_form_field_values(
        writer.pages[0],
        {
            # Sektion
            CHAPTER_FIELD: anmalan.chapter,
            # Festansvarig
            FA_NAME_FIELD: anmalan.fa.name,
            FA_PHONE_FIELD: anmalan.fa.phone,
            # Serveringsansvarig
            SA_NAME_FIELD: anmalan.sa.name,
            SA_PHONE_FIELD: anmalan.sa.phone,
            # Brandansvarig
            BA_NAME_FIELD: anmalan.ba.name,
            BA_PHONE_FIELD: anmalan.ba.phone,
            # Utrymningsledare:
            UL_NAME_FIELD: anmalan.ul.name,
            UL_PHONE_FIELD: anmalan.ul.phone,
            # Plats:
            EVENT_LOCATION_FIELD: anmalan.location,
            ADDRESS_FIELD: anmalan.address,
            # Sektionslokalsansvarig:
            CHAPTER_HALL_NAME_FIELD: anmalan.chapter_hall.name,
            CHAPTER_HALL_PHONE_FIELD: anmalan.chapter_hall.phone,
            # Typ av sammankomst:
            EVENT_TYPE_FIELD: anmalan.event_type,
            EVENT_DATE_FIELD: anmalan.date,
            EVENT_START_TIME_FIELD: anmalan.start_time,
            EVENT_END_TIME_FIELD: anmalan.end_time,
            PERSON_COUNT_FIELD: str(anmalan.person_count),
            GRILL_FIELD: "/On" if anmalan.grill else "/Off",
            # Alkoholservering
            ALCOHOL_YES_FIELD: (
                "/On" if anmalan.alcohol else "/Off"
            ),  # Checkboxes typically use /On or /Yes
            ALCOHOL_NO_FIELD: (
                "/On" if not anmalan.alcohol else "/Off"
            ),  # Checkboxes typically use /On or /Yes
            PERMANENT_SERVING_FIELD: "/On" if anmalan.permanent_serving else "/Off",
            TEMPORARY_PERMIT_FIELD: "/On" if anmalan.temporary_permit else "/Off",
            EXTENDED_GUESTS_FIELD: "/On" if anmalan.extended_guests else "/Off",
            EXTENDED_AREA_FIELD: "/On" if anmalan.extended_area else "/Off",
        },
        auto_regenerate=False,
    )

    # Return the pdf as an in-memory stream
    pdf_buffer = io.BytesIO()
    writer.write(pdf_buffer)
    pdf_buffer.seek(0)  # Rewind the buffer to the beginning for reading
    return pdf_buffer
