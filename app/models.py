from pydantic import BaseModel, Field


class Person(BaseModel):
    name: str = Field(
        ..., min_length=2, max_length=100, description="The full name of the person"
    )
    phone: str = Field(
        ..., min_length=10, max_length=15, description="The phone number of the person"
    )


class Festanmalan(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100,
        description="The name of the festanmälan",
    )
    chapter: str = Field(
        default="IN- Sektionen för Informations- och Nanoteknik",
        min_length=2,
        max_length=100,
        description="The name of the chapter",
    )
    fa: Person = Field(..., description="The full name of the festansvarig")
    sa: Person = Field(..., description="The full name of the serveringsansvarig")
    ba: Person = Field(..., description="The full name of the brandansvarig")
    ul: Person = Field(..., description="The full name of the utrymningsledare")
    location: str = Field(
        default="Kistan 2.0", description="The name of the event premises"
    )
    address: str = Field(
        default="Kistagången 16", description="The address of the event premises"
    )
    chapter_hall: Person = Field(
        ...,
        description="The name of the chapter hall responsible (usually the President)",
    )
    event_type: str = Field(default="Pub", description="The type of event")
    date: str = Field(..., description="The date of the event")
    start_time: str = Field(..., description="The start time of the event")
    end_time: str = Field(..., description="The end time of the event")
    person_count: int = Field(
        ..., description="The number of people attending the event"
    )
    grill: bool = Field(
        default=False, description="Whether grilling will occur during the event"
    )
    alcohol: bool = Field(
        default=False, description="Whether alcohol will be served during the event"
    )
    permanent_serving: bool = Field(
        default=False, description="Whether the premises has a permanent serving permit"
    )
    temporary_permit: bool = Field(
        default=False, description="Whether the event has a temporary permit"
    )
    extended_guests: bool = Field(
        default=False,
        description="Whether the allowed guests for the permit are extended",
    )
    extended_area: bool = Field(
        default=False, description="Whether the serving area is extended"
    )
