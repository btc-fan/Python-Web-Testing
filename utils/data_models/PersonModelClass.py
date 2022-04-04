from marshmallow_dataclass import dataclass


@dataclass
class PersonModel:
    UUID: str
    firstname: str
    lastname: str
    ssn: str
    address: str
    city: str
    zip: str
    state: str
    dob: str
    apt: str
    telephone: str
