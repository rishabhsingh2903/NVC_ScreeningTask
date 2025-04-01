from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True,index=True)
    status = Column(String, default='pending')
    filters = Column(String)

    data = relationship("DataRow", back_populates="task")


class DataRow(Base):
    __tablename__ ="data_rows"
    id = Column(Integer, primary_key=True,index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    source = Column(String)
    company_name = Column(String)
    model_name = Column(String)
    date = Column(Date)
    price = Column(Float)

    task  = relationship("Task", back_populates="data")

    