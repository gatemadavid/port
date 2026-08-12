from sqlalchemy import DateTime, Text, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    image: Mapped[str | None] = mapped_column(String(255), nullable=True, default="default.jpg")

    posts: Mapped[list["Post"]] = relationship(back_populates="author", cascade="all, delete-orphan")

    @property
    def image_url(self) -> str:
        if self.image:
            return f"/media/{self.image}"
        return "/static/me-hero.jpg"
    

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime (timezone=True), nullable=False)

    author: Mapped["User"] = relationship( back_populates="posts")

    # comments: Mapped[list["Comments"]] = relationship("Comments", back_populates="post")