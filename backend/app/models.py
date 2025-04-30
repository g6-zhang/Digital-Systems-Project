from sqlalchemy import Column, Integer, String,Boolean
from .database import Base

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from datetime import datetime
from sqlalchemy import DateTime

from datetime import date
from sqlalchemy import Date

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    avatar_url = Column(String, default="/static/images/avatar.png")
    has_played_game = Column(Boolean, default=False)
    last_score = Column(Integer, default=0)

    plays_today = Column(Integer, default=0)
    last_play_date = Column(Date, default=date.today)
    has_earned_discount = Column(Boolean, default=False)

    discount_used = Column(Boolean, default=False)

class FavoriteAnimal(Base):
    __tablename__ = "favorite_animals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    animal_name = Column(String, nullable=False)

    user = relationship("User", backref="favorite_animals")

class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)