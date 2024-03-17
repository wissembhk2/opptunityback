
from app.utils.database import sessionLocal
from app.models.schema import UserInformationschema
from app.models.users import Users,Usersinformations


def updateknowdetails(data:UserInformationschema,email):
        db = sessionLocal()
        user = db.query(Users).filter(Users.email == email ).first()
       # data.user_id=user.id
        userinfo=db.query(Usersinformations).filter(Usersinformations.user_id==user.id).first()
        userinfo.address=data.address
        userinfo.phone=data.phone
        userinfo.gender=data.gender
        userinfo.birthdate=data.birthdate        
        db.add(userinfo)
        db.commit()
        return data


def updatequalificationsdetails(data:UserInformationschema,email):
        db = sessionLocal()
        
        user = db.query(Users).filter(Users.email == email ).first()
       # data.user_id=user.id
        userinfo=db.query(Usersinformations).filter(Usersinformations.user_id==user.id).first()
        userinfo.skills=data.skills
        userinfo.languages=data.languages
        db.add(userinfo)
        db.commit()
        return data

def updatedescription(data:UserInformationschema,email):
        db = sessionLocal()
        
        user = db.query(Users).filter(Users.email == email ).first()
       # data.user_id=user.id
        userinfo=db.query(Usersinformations).filter(Usersinformations.user_id==user.id).first()
        userinfo.description=data.description
        db.add(userinfo)
        db.commit()
        return data

def getinfos(email):
        db = sessionLocal()
        user = db.query(Users).filter(Users.email == email ).first()
        userinfo=db.query(Usersinformations).filter(Usersinformations.user_id==user.id).first()
        return {'userinfo':userinfo,'user':user}

        