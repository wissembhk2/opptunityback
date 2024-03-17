from app.utils.database import base
from sqlalchemy import Column,  Integer, String,Boolean,DateTime, ForeignKey , Date,BigInteger
import datetime
from datetime import date
from sqlalchemy.dialects.postgresql import  JSONB  # Or use JSON
from app.models.schema import UserSignup,UserOnboarding
from sqlalchemy.orm import relationship

class Users(base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, auto_increment=True)
    name = Column(String)
    email = Column(String,unique=True)
    password = Column(String)
    status = Column(Boolean)
    google_id = Column(String)
    microsoft_id=Column(Integer)
    is_microsoft_id=Column(Boolean)
    is_google_account= Column(Boolean)
    created_at=Column(DateTime, default=datetime.datetime.utcnow)
    confirmation_token=Column(String)
    type=Column(String)



    def __init__(self, user_signup: UserSignup):
        self.name = user_signup.name
        self.email = user_signup.email
        self.password = user_signup.password
        self.status = user_signup.status
        self.google_id = user_signup.google_id
        self.is_google_account = user_signup.is_google_account
        self.microsoft_id = user_signup.microsoft_id
        self.is_microsoft_account = user_signup.is_microsoft_account
        self.confirmation_token=user_signup.confirmation_token
        self.type=user_signup.type
  

class Usersinformations(base):
    __tablename__ = "users_informations"
    id = Column(Integer, primary_key=True, auto_increment=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))  # Define the foreign key
    # user = relationship("Users", back_populates="informations", cascade="all, delete")
    age = Column(String)
    country= Column(String)
    languages = Column(JSONB)  # Define an array of JSONB objects
    phone = Column(String)
    address= Column(String)
    gender = Column(String)
    current_location= Column(String)
    skills=Column(JSONB)
    description=Column(String)
    birthdate=Column(Date)
    def __init__(self, user_signup: UserOnboarding):
        self.user_id = user_signup.user_id
        self.languages = user_signup.languages
        self.country = user_signup.country
        self.age = user_signup.age
      