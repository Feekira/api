from datetime import datetime
from pydantic import BaseModel
from datetime import time

class DeviceBase(BaseModel):
    ip: str
    uniorg: str
    identifier: str

class DeviceRequest(DeviceBase):
    ...

class DeviceResponse(DeviceBase):
    id: int

    class Config:
        orm_mode = True

class ScheduleBase(BaseModel):
    start_schedule_weekday: time
    finish_schedule_weekday: time
    start_schedule_weekend: time
    finish_schedule_weekend: time
    mode: int
    device_id: int

class ScheduleRequest(ScheduleBase):
    ...

class ScheduleResponse(ScheduleBase):
    id: int
    
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    password: int
    coercion: int
    phone: str

class UserRequest(UserBase):
    ...

class UserResponse(UserBase):
    id :int

    class Config:
        orm_mode = True

class GpioBase(BaseModel):
    pin:int
    value:int
    created_At: datetime
    device_id:int

class GpioRequest(GpioBase):
    ...

class GpioResponse(UserBase):
    id :int

    class Config:
        orm_mode = True