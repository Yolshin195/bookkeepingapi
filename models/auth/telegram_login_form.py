from pydantic import BaseModel


class TelegramLoginModel(BaseModel):
    username: str
