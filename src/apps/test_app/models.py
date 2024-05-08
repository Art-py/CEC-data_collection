from sqlalchemy import Column, Integer, MetaData, String, Table
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base()


test_model_model = Table(
    "test_model",
    metadata,
    # Main fields
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
)


class TestModelModel(Base):
    __tablename__ = "test_model"

    id = Column(Integer, primary_key=True)
    name = Column(String)
