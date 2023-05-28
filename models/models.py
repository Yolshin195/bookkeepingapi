import datetime
import uuid
from sqlalchemy import MetaData, Table, Column, ForeignKey, Integer, String, TIMESTAMP, UUID, JSON

metadata = MetaData(naming_convention={
    "table_prefix": "bookkeeping_api_"
})

roles = Table(
    "roles",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

users = Table(
    "users",
    metadata,
    Column("id", UUID, primary_key=True, default=uuid.uuid4),
    Column("email", String, nullable=False, unique=True),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("date_created", TIMESTAMP, nullable=False, default=datetime.datetime.utcnow),
    Column("role_id", UUID, ForeignKey("roles.id"))
)
