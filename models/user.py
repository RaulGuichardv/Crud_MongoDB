from pydantic import BaseModel

class User(BaseModel):
    id: str | None
    name: str
    emal: str
    password: str