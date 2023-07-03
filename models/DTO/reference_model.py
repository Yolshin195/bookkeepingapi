from uuid import UUID

from pydantic import BaseModel


class ReferenceModel(BaseModel):
    id: UUID
    code: str
    name: str
