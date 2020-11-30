from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Boolean,Date,Time,ForeignKey,Text
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    user_email = Column(String,primary_key=True)
    name = Column(String)
    verified = Column(Boolean)
    hash = Column(Text)
    
class Membership(Base):
    __tablename__ = "memberships"
    membership_id = Column(Integer,primary_key = True)
    user_email = Column(String,ForeignKey('users.user_email'))
    organization_id = Column(Integer,ForeignKey('organizations.organization_id'))
    admin = Column(Boolean)

class Organization(Base):
    __tablename__ = "organizations"
    organization_id = Column(Integer,primary_key=True)
    name = Column(String)

class Attendance(Base):
    __tablename__ = "attendance"
    attendance_id = Column(Integer,primary_key = True)
    user_email = Column(String, ForeignKey('users.user_email'))
    event_id = Column(Integer,ForeignKey('events.event_id'))
    registration_date = Column(Date)
    registration_time = Column(Time)

class Event(Base):
    __tablename__ = "events"
    event_id = Column(Integer,primary_key = True)
    organization_id = Column(Integer,ForeignKey('organizations.organization_id'))
    event_date = Column(Date)
    event_time = Column(Time)
    location = Column(String)
    capacity = Column(Integer)
