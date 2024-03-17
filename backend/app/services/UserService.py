from app.models.users import Users,Usersinformations
from app.models.schema import UserSignup,UserOnboarding
from app.utils.database import sessionLocal
import bcrypt
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from itsdangerous import URLSafeTimedSerializer
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fastapi.responses import RedirectResponse
import jwt
import datetime
def add_user(user_data:UserSignup):
    
    # Create an instance of the Users class with the provided details
    hashed_pwd=bcrypt.hashpw(user_data.password.encode('utf-8'), bcrypt.gensalt())
    print(hashed_pwd)
    user_data.password = hashed_pwd.decode('utf-8')
    print(user_data)
    # Create a new database session
    session = sessionLocal()
    user= Users(user_data)
    try:
        # Add the new user to the session and commit the transaction
        session.add(user)
        session.commit()
        return {"message": f"User {user_data.name} added successfully."}  # Success response
    except IntegrityError as e:
        # Rollback the transaction if there's a uniqueness constraint violation (e.g., email already exists)
        session.rollback()
        raise HTTPException(status_code=409, detail=f"The email {user_data.email} is already in use.")        # Handle other unexpected errors
    finally:
        # Close the session whether or not there was an error
        session.close()

def add_google_user(user_data:UserSignup):
            session = sessionLocal()

            user= Users(user_data)
            try:
                # Add the new user to the session and commit the transaction
                session.add(user)
                session.commit()
                return {"message": f"User {user_data.name} added successfully."}  # Success response
            except IntegrityError as e:
                # Rollback the transaction if there's a uniqueness constraint violation (e.g., email already exists)
                session.rollback()
                raise HTTPException(status_code=409, detail=f"The email {user_data.email} is already in use.")        # Handle other unexpected errors
            finally:
                # Close the session whether or not there was an error
                session.close()


def send_email(email,token):


# Your Google email account credentials
    google_email = "wissem@opptunity.com"
    google_password = "orne mnju zbxx aueu "  # Use an App Password if 2-Step Verification is enabled

    # Email content
    sender_email = google_email
    subject = "Opptunity account verification"
    body = "This is a test email sent from a Python script using Google SMTP server. " + "http://127.0.0.1:3000/emailverified/"+token

    # Set up the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Google's SMTP server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # For starttls

    # Send the email
    try:
        # Connect to the Google SMTP server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection with TLS
        server.login(google_email, google_password)
        server.sendmail(sender_email, email, message.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        server.quit()
SECRET_KEY = "your_secret_key_here"  # Use a strong, unique key for your application
SALT = "email_confirm_salt"
def generate_confirmation_token(email_address: str):
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    token = serializer.dumps(email_address, salt=SALT)
    db = sessionLocal()
    try:
        # Query the database for the user with the given email address
        user = db.query(Users).filter(Users.email == email_address).first()

        if user:
            # If the user exists, update the user's confirmation token
            user.confirmation_token = token

            # Commit the changes to the database
            db.commit()

            # Optionally, you could return both the user and the token if needed
            send_email(email_address,token)
            return token
        else:
            # If no user exists with the given email, handle accordingly
            # For example, raise an exception or return None
            raise Exception(f"No user found with email {email_address}")

    except Exception as e:
        # If there's an error, rollback the transaction and handle it (e.g., by logging or raising)
        db.rollback()
        raise e

    finally:
        # Close the session whether or not there was an error
        db.close()

def confirm_token(token: str, expiration=3600):
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    try:
        email_address = serializer.loads(
            token,
            salt=SALT,
            max_age=expiration
        )
    except Exception:  # You can be more specific with the exception handling
        return False
    try:
        # Query the database for the user with the given email address
        db = sessionLocal()
        user = db.query(Users).filter((Users.email == email_address) & (Users.confirmation_token== token)).first()

        if user:
            # If the user exists, update the user's confirmation token
            user.status = True
            user.confirmation_token=""

            # Commit the changes to the database
            db.commit()
            # return RedirectResponse(url="http://127.0.0.1:3000/emailverified", status_code=303)
        else:
            # If no user exists with the given email, handle accordingly
            # For example, raise an exception or return None
            raise Exception(f"No user found with email {email_address}")
    except Exception as e:
        # If there's an error, rollback the transaction and handle it (e.g., by logging or raising)
        db.rollback()
        raise e

    finally:
        # Close the session whether or not there was an error
        db.close()

def onboarding(data:UserOnboarding):
        db = sessionLocal()
        user = db.query(Users).filter(Users.email == data.email ).first()
        data.user_id=user.id
        userinfo=Usersinformations(data)
     
        db.add(userinfo)
        db.commit()
        return data


JWT_SECRET = 'your_jwt_secret'
JWT_ALGORITHM = 'HS256'
def sign_in(email, submitted_password):
    # Create a new database session
    session = sessionLocal()
    
    try:
        # Query the database for the user by email
        user = session.query(Users).filter(Users.email == email).first()
        # If a user is found, check the submitted password against the stored hash
        if user and bcrypt.checkpw(submitted_password.encode('utf-8'), user.password.encode('utf-8')):
            # Password is correct
            print(f"User {user.name} signed in successfully.")
            token_data = {
                "user_id": user.id,  # Include user-specific data
                "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=3600),  # Token expiration time (e.g., 1 hour)
                "email":user.email,
                "type":user.type
            }
            token = jwt.encode(token_data, JWT_SECRET, algorithm=JWT_ALGORITHM)
            return token
        else:
            # User not found or password is incorrect
            print("Invalid login credentials.")
            return False
    except Exception as e:
        # If there's an error, print the error
        print(f"Error signing in: {e}")
        return False
    finally:
        # Close the session whether or not there was an error
        session.close()


def google_sign_in(email,google_id):
    # Create a new database session
    session = sessionLocal()
    print(google_id)
    
    try:
        # Query the database for the user by email
        user = session.query(Users).filter(Users.email == email , Users.google_id==google_id).first()
        # If a user is found, check the submitted password against the stored hash
        if user :
            # Password is correct
            print(f"User {user.name} signed in successfully.")
            token_data = {
                "user_id": user.id,  # Include user-specific data
                "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=3600),  # Token expiration time (e.g., 1 hour)
                "email":user.email,
                "type":user.type
            }
            token = jwt.encode(token_data, JWT_SECRET, algorithm=JWT_ALGORITHM)
            return token
        else:
            # User not found or password is incorrect
            print("Invalid login credentials.")
            return False
    except Exception as e:
        # If there's an error, print the error
        print(f"Error signing in: {e}")
        return False
    finally:
        # Close the session whether or not there was an error
        session.close()