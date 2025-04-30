import os
from pathlib import Path
from fastapi import APIRouter, UploadFile, File, Depends, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "static" / "avatars"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/upload-avatar")
async def upload_avatar(
    request: Request,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    user_id = request.session.get("user_id")
    if not user_id:
        return JSONResponse(content={"detail": "Unauthorized"}, status_code=401)

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return JSONResponse(content={"detail": "User not found"}, status_code=404)

    file_path = UPLOAD_DIR / f"{user.id}.png"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    avatar_url = f"/static/avatars/{user.id}.png"
    user.avatar_url = avatar_url
    db.commit()

    return {"avatar_url": avatar_url}