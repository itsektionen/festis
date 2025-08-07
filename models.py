from pydantic import BaseModel


class Person(BaseModel):
    name: str
    phone: str

class Festanmalan(BaseModel):
    name: str
    phone: str
    chapter: str
    sa: Person
    ba: Person
    ul: Person
    chapter_hall: Person
    date: str
    time: str
    location: str
    event_type: str
    alcohol: bool
    permanent_serving: bool
    person_count: int
    address: str