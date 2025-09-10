from sqlalchemy import String, Table, Column
from sqlalchemy.sql.sqltypes import Integer
from config.db import meta, engine

vehicles = Table(
    "Vehiculos", 
    meta,
    Column("id", Integer, primary_key=True),
    Column("marca", String(100), nullable=False),
    Column("sucursal", String(100), nullable=False),
    Column("nombre_persona", String(100), nullable=False)
    )

meta.create_all(engine)