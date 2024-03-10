from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Time
from database.connection import Base
import datetime
import time

class Device(Base):
    __tablename__ = "device"

    id: int = Column(Integer, primary_key=True, index=True)
    ip: str = Column(String(12), nullable=False)
    uniorg: str = Column(String(12), nullable=False)
    identifier: str = Column(String(20), nullable=False)

class Schedule(Base):
    __tablename__ = "schedule"
    
    id:int = Column(Integer, primary_key=True, index=True)
    start_schedule_weekday: time = Column(Time, nullable=False)
    finish_schedule_weekday: time = Column(Time, nullable=False)
    start_schedule_weekend: time = Column(Time, nullable=False)
    finish_schedule_weekend: time = Column(Time, nullable=False)
    mode: int = Column(Integer, nullable=False)
    device_id: int = Column(Integer, ForeignKey("device.id"), nullable=False)

class User(Base):
    __tablename__ = "user"

    id:int = Column(Integer, primary_key=True, index=True)
    name:str = Column(String(50), nullable=False)
    password: int = Column(Integer, nullable=False)
    coercion: int = Column(Integer, nullable=False)
    phone: str = Column(String, nullable=False)
    # PHOTO

class Gpio(Base):
    __tablename__ = "pins"

    id:int = Column(Integer, primary_key=True, index=True)
    pin:int = Column(Integer, nullable=False)
    value:int = Column(Integer, nullable=False)
    created_At:datetime = Column(DateTime, default=datetime.datetime.now())
    device_id:int = Column(Integer, ForeignKey("device.id"), nullable=False)