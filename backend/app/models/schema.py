from pydantic import BaseModel
from typing import List
from datetime import date
class UserSignup(BaseModel):
    name: str
    email: str
    password: str= None
    status: bool=False
    google_id: str = None  # Assuming google_id can be optional
    is_google_account: bool = False  # Defaulting to False if not provided
    microsoft_id: int = None  # Assuming google_id can be optional
    is_microsoft_account: bool = False  # Defaulting to False if not provided
    confirmation_token: str = None
    type: str = "candidate"

class Language(BaseModel):
    label: str
    value: str
    proficiency: str = None

class Skills(BaseModel):
    label: str
    proficiency: str = None

class UserOnboarding(BaseModel):
    email:str
    age:str
    country:str
    languages:List[dict]
    user_id:int=None
        

class UserSignin(BaseModel):
    email:str
    password:str=None
    google_id:str=None

class UserInformationschema(BaseModel):
    phone:str=None
    address:str=None
    gender:str=None
    current_location:str=None
    skills:List[dict]=None
    user_id:int=None
    languages:List[dict]=None
    description:str=None
    birthdate:date=None


    
