from fastapi import FastAPI, Depends, UploadFile, File, Request, HTTPException
from starlette.middleware.sessions import SessionMiddleware 
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse
from pathlib import Path
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
import shutil
import os

from app.routes import auth
from app.database import get_db, engine
from app import models
from app.utils import hash_password, verify_password

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    SessionMiddleware,
    secret_key="mysupersecret",
    session_cookie="session",             
    same_site="lax",                      
    https_only=False                      
)

app.include_router(auth.router)

STATIC_DIR = Path(__file__).resolve().parent

app.mount("/images", StaticFiles(directory=STATIC_DIR / "images"), name="images")
app.mount("/styles", StaticFiles(directory=STATIC_DIR / "styles"), name="styles")
app.mount("/animals", StaticFiles(directory=STATIC_DIR / "animals"), name="animals")
app.mount("/static", StaticFiles(directory=STATIC_DIR / "static"), name="static")
app.mount("/static/avatars", StaticFiles(directory=STATIC_DIR / "static" / "avatars"), name="avatars")
app.mount("/static/uploads", StaticFiles(directory=STATIC_DIR / "images" / "uploads"), name="uploads")
app.mount("/game-static", StaticFiles(directory=STATIC_DIR / "game"), name="game-static")  
app.mount("/game", StaticFiles(directory=STATIC_DIR / "game"), name="game")  

@app.get("/", response_class=FileResponse)
async def get_index():
    return FileResponse(STATIC_DIR / "index.html")

@app.get("/login", response_class=FileResponse)
async def get_login():
    return FileResponse(STATIC_DIR / "login.html")

@app.get("/register", response_class=FileResponse)
async def get_register():
    return FileResponse(STATIC_DIR / "register.html")

@app.get("/reset-password", response_class=FileResponse)
async def get_reset_password():
    return FileResponse(STATIC_DIR / "reset-password.html")

@app.get("/tickets", response_class=FileResponse)
async def get_tickets():
    return FileResponse(STATIC_DIR / "tickets.html")

@app.get("/play-game", response_class=FileResponse)
async def get_game():
    return FileResponse(STATIC_DIR / "game" / "game.html")

@app.get("/map", response_class=FileResponse)
async def get_map():
    return FileResponse(STATIC_DIR / "map.html")

@app.get("/animals", response_class=FileResponse)
async def get_animals():
    return FileResponse(STATIC_DIR / "animals.html")

@app.get("/home", response_class=FileResponse)
async def get_home():
    return FileResponse(STATIC_DIR / "templates" /"index2.html")

@app.get("/profile", response_class=FileResponse)
async def get_profile():
    return FileResponse(STATIC_DIR / "templates" /"profile.html")

@app.get("/map2", response_class=FileResponse)
async def get_map2():
    return FileResponse(STATIC_DIR / "templates" /"map2.html")

@app.get("/tickets2", response_class=FileResponse)
async def get_tickets2():
    return FileResponse(STATIC_DIR / "templates" /"tickets2.html")

@app.get("/animals2", response_class=FileResponse)
async def get_animals2():
    return FileResponse(STATIC_DIR / "templates" /"animals2.html")

@app.get("/users", response_class=JSONResponse)
def read_users(db: Session = Depends(get_db)):
    try:
        users = db.query(models.User).all()
        return [{"id": u.id, "email": u.email, "full_name": u.full_name, "hashed_password": u.hashed_password} for u in users]
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/user/me")
def get_user_info(request: Request, db: Session = Depends(get_db)):
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    avatar_url = user.avatar_url or f"/static/avatars/default.png"
    return {
        "full_name": user.full_name,
        "avatar_url": avatar_url
    }

@app.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/", status_code=302)

class UpdateUserInfo(BaseModel):
    full_name: str

@app.post("/user/update")
def update_user_info(data: UpdateUserInfo, request: Request, db: Session = Depends(get_db)):
    user_id = request.session.get("user_id")
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.full_name = data.full_name
    db.commit()
    return {"message": "User info updated"}

class RegisterRequest(BaseModel):
    full_name: str
    email: EmailStr
    password: str

@app.post("/register")
def register_user(data: RegisterRequest, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = models.User(
        full_name=data.full_name,
        email=data.email,
        hashed_password=hash_password(data.password),
        avatar_url="/static/avatars/default.jpg"
    )
    db.add(new_user)
    db.commit()
    return {"message": "User created successfully"}

@app.post("/upload-avatar")
async def upload_avatar(
    request: Request,
    avatar: UploadFile = File(...), 
    db: Session = Depends(get_db)
):
    try:
        user_id = request.session.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Unauthorized")

        user = db.query(models.User).filter(models.User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        avatar_dir = STATIC_DIR / "static" / "avatars"
        avatar_dir.mkdir(parents=True, exist_ok=True)
        avatar_path = avatar_dir / f"{user.id}.jpg"

        with open(avatar_path, "wb") as buffer:
            shutil.copyfileobj(avatar.file, buffer)

        user.avatar_url = f"/static/avatars/{user.id}.jpg"
        db.commit()

        return {"avatar_url": user.avatar_url}
    except Exception as e:
        print("❌ Upload failed:", e)
        raise HTTPException(status_code=500, detail="Upload failed")

from app.schemas import PasswordResetRequest
from app.crud import update_user_password

@app.post("/reset-password")
def reset_password(data: PasswordResetRequest, db: Session = Depends(get_db)):
    if data.new_password != data.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    user = update_user_password(db, data.email, data.full_name, data.new_password)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found with given email and name")

    return {"message": "Password updated successfully"}

@app.post("/login")
async def login(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    email = form.get("email")
    password = form.get("password")

    user = db.query(models.User).filter(models.User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        return JSONResponse(content={"success": False, "message": "Invalid email or password"}, status_code=401)

    request.session["user_id"] = user.id

    return JSONResponse(content={"success": True, "message": "Login successful"})

from datetime import date

@app.get("/api/game/status")
def get_game_status(request: Request, db: Session = Depends(get_db)):
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")

    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.last_play_date != date.today():
        user.plays_today = 0
        user.last_play_date = date.today()
        db.commit()

    return {
        "plays_today": user.plays_today,
        "has_earned_discount_before": user.has_earned_discount
    }

from fastapi import Form

@app.post("/api/game/finish")
def finish_game(
    request: Request,
    score: int = Form(...),
    db: Session = Depends(get_db)
):
    user_id = request.session.get("user_id")
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    from datetime import date
    if user.last_play_date != date.today():
        user.plays_today = 0
        user.last_play_date = date.today()

    user.plays_today += 1

    if score == 5 and user.plays_today <= 2 and not user.has_earned_discount:
        user.has_earned_discount = True

    db.commit()
    return {"message": "Game recorded"}

@app.get("/api/game/result")
def get_game_result(request: Request, db: Session = Depends(get_db)):
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")

    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "score": user.last_score,
        "has_earned_discount": user.has_earned_discount,
        "discount_used": user.discount_used 
    }

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="app/templates")

@app.get("/feedback", response_class=HTMLResponse)
async def get_feedback_page(request: Request):
    return templates.TemplateResponse("feedback.html", {"request": request})

from app.models import Feedback  

@app.post("/feedback")
async def submit_feedback(request: Request, feedback: str = Form(...), db: Session = Depends(get_db)):
    fb = Feedback(content=feedback)
    db.add(fb)
    db.commit()
    return RedirectResponse(url="/feedback", status_code=303)

@app.get("/view-feedbacks", response_class=HTMLResponse)
def view_feedbacks(db: Session = Depends(get_db)):
    feedbacks = db.query(Feedback).order_by(Feedback.created_at.desc()).all()
    html = "<h2>All User Feedback</h2><ul>"
    for fb in feedbacks:
        html += f"<li>{fb.created_at.strftime('%Y-%m-%d %H:%M:%S')} - {fb.content}</li>"
    html += "</ul>"
    return html

from typing import List
from app.models import FavoriteAnimal  

@app.post("/favorites/toggle")
def toggle_favorite(
    animal_name: str,
    request: Request,
    db: Session = Depends(get_db)
):
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")

    existing = db.query(FavoriteAnimal).filter_by(user_id=user_id, animal_name=animal_name).first()
    if existing:
        db.delete(existing)
        db.commit()
        return {"status": "removed"}
    else:
        new_fav = FavoriteAnimal(user_id=user_id, animal_name=animal_name)
        db.add(new_fav)
        db.commit()
        return {"status": "added"}

@app.get("/favorites", response_model=List[str])
def get_favorites(
    request: Request,
    db: Session = Depends(get_db)
):
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")

    favorites = db.query(FavoriteAnimal).filter_by(user_id=user_id).all()
    return [f.animal_name for f in favorites]

from fastapi import Form, Request

@app.post("/user/change-password")
def change_password(
    request: Request,
    old_password: str = Form(...),
    new_password: str = Form(...),
    db: Session = Depends(get_db)
):
    user_id = request.session.get("user_id")
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(old_password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Old password is incorrect")

    user.hashed_password = hash_password(new_password)
    db.commit()
    return {"message": "Password changed"}

@app.post("/api/game/consume-discount")
def consume_discount(request: Request, db: Session = Depends(get_db)):
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")

    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.has_earned_discount and not user.discount_used:
        user.discount_used = True
        db.commit()

    return {"message": "Discount marked as used"}