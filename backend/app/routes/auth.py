from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse, RedirectResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get("/logout")
async def logout():
    response = RedirectResponse(url="/")
    response.delete_cookie("user_id")
    return response


@router.post("/reset-password")
async def reset_password_json(
    request: Request,
    db: Session = Depends(get_db)
):
    data = await request.json()
    email = data.get("email")
    full_name = data.get("full_name")
    new_password = data.get("new_password")

    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        return JSONResponse(status_code=400, content={"success": False, "message": "User does not exist."})
    
    if user.full_name != full_name:
        return JSONResponse(status_code=400, content={"success": False, "message": "Full name does not match."})

    if len(new_password) < 8:
        return JSONResponse(status_code=400, content={"success": False, "message": "Password must be at least 8 characters long."})

    user.hashed_password = pwd_context.hash(new_password)
    db.commit()

    return JSONResponse(content={"success": True, "message": "Password reset successful."})
