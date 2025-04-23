from sqlalchemy import Table, Column, String, DateTime
from sqlalchemy.sql import func
from database import metadata
import uuid

users = Table(
    "users", metadata,
    Column("id", String, primary_key=True, default=lambda: str(uuid.uuid4())),
    Column("name", String, nullable=False),
    Column("email", String, unique=True, nullable=False),
    Column("password_hash", String, nullable=False),
    Column("created_at", DateTime, default=func.now())
)
