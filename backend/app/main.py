from fastapi import APIRouter, FastAPI
from app.utils.database import create_db
from app.services.UserService import *
from fastapi.middleware.cors import CORSMiddleware
from app.models.schema import UserSignup , UserSignin ,UserOnboarding,UserInformationschema
from app.services.UserInformationsService import updateknowdetails,updatequalificationsdetails,updatedescription,getinfos
app = FastAPI()
router = APIRouter(prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

create_db()


@router.post('/signup')
async def signup(user_data:UserSignup):
    success = add_user(
        user_data
    )
    return success

@router.post('/signup_google')
async def signup(user_data:UserSignup):
    success = add_google_user(
        user_data
    )
    return success

@router.post('/signin')
async def signin(user_data:UserSignin):
    return sign_in(user_data.email, user_data.password)

@router.post('/google_signin')
async def signingoogle(user_data:UserSignin):
    return google_sign_in(user_data.email,user_data.google_id)
    
@router.post('/tokengenerate')
async def tokengenerator(email:str):
    return generate_confirmation_token(email)

@router.get('/tokenvalidation')
async def tokenvalidator(token:str):
    return confirm_token(token)

@router.post('/testonboard')
async def onboard(data:UserOnboarding):
    return onboarding(data)

@router.post('/email')
async def mail():
    return send_email()

@router.post('/details')
async def details(data:UserInformationschema,email:str):
    return updateknowdetails(data,email)

@router.post('/qualifications')
async def qualifications(data:UserInformationschema,email:str):
    print(data)
    return updatequalificationsdetails(data,email)

@router.post('/description')
async def update_description(data:UserInformationschema,email:str):
    print(data)
    return updatedescription(data,email)

@router.get('/userinfo')
async def userinfo(email:str):
    
    return getinfos(email)

app.include_router(router)
