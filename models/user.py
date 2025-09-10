from sqlalchemy import Table, Column, String, Integer
from config.db import meta, engine

users = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True),
    Column("username", String(50), unique=True, nullable=False),
    Column("password", String(255), nullable=False),  # hash de la contraseña
)

meta.create_all(engine)
