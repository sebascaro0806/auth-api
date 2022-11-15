from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from src.config.db import engine, meta_data

users = Table("users", meta_data,
            Column("id", String, primary_key=True),
            Column("email", String, nullable=False),
            Column("password", String, nullable=False)
        )

meta_data.create_all(engine)