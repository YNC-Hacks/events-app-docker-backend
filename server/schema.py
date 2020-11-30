from pydantic import BaseModel,EmailStr
from typing import Optional
import datetime


class User(BaseModel):
    user_email: str
    name: str

class Membership(BaseModel):
    membership_id =int
    user_email = str
    organization_id = int
    admin = bool

    class Config:
        orm_mode = True

class Organization(BaseModel):
    organization_id = int
    name = str

class Attendance(BaseModel):
    attendance_id = int
    user_email = str
    event_id = int
    registration_date = datetime.date
    registration_time = datetime.time

class Event:
    event_id = int
    organization_id = int
    event_date = datetime.date
    event_time = datetime.time
    location = str
    capacity = int

