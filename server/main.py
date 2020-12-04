import uvicorn
from fastapi import FastAPI,Request
from typing import Optional
import os
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from pydantic import BaseModel
from sqlalchemy.sql import text

import secrets

from models import User as ModelUser,\
                   Membership as ModelMembership,\
                   Organization as ModelOrganization,\
                   Attendance as ModelAttendance,\
                   Event as ModelEvent

from schema import User as SchemaUser,\
                   Membership as SchemaMembership,\
                   Organization as SchemaOrganization,\
                   Attendance as SchemaAttendance,\
                   Event as SchemaEvent

from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

class User(BaseModel):
    name: str
    user_email: str



app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

@app.get("/")
def return_response():
    return "Hello!"

@app.post('/users/create')
def create_user(user:SchemaUser):
    db_user = ModelUser(
        user_email = user.user_email,
        name = user.name,
        verified = False,
        hash = secrets.token_hex(nbytes=16)
    )
    db.session.add(db_user)
    db.session.commit()
    return user

@app.get('/users/check')
def check_user_email(email:str):
    return db.session.query(ModelUser.user_email).filter_by(user_email=email).scalar() is not None



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)