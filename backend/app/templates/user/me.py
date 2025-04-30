from fastapi import APIRouter, Depends, Request, Form
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.get("/user/me")
def get_current_user_info(request: Request, db: Session = Depends(get_db)):
    user_id = request.session.get("user_id")
    if not user_id:
        return {"detail": "Not logged in"}
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return {"detail": "User not found"}

    return {
        "full_name": user.full_name,
        "avatar_url": user.avatar_url
    }


@router.post("/user/change-password")
def change_password(
    request: Request,
    old_password: str = Form(...),
    new_password: str = Form(...),
    db: Session = Depends(get_db)
):
    user_id = request.session.get("user_id")
    if not user_id:
        return {"detail": "Not logged in"}

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return {"detail": "User not found"}

    if not pwd_context.verify(old_password, user.hashed_password):
        return {"detail": "Incorrect old password"}

    user.hashed_password = pwd_context.hash(new_password)
    db.commit()
    return {"message": "Password changed successfully"}