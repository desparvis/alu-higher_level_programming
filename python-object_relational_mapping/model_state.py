#!/usr/bin/python3
"""
This script contains the class definition of a State and an instance
Base = declarative_base(). It connects to a MySQL server running on localhost
at port 3306.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that represents the 'states' table in MySQL database.

    Attributes:
        id (int): Primary key, auto-incremented, non-nullable.
        name (str): String of max 128 characters, non-nullable.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://your_username:your_password@localhost/your_database',
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)
