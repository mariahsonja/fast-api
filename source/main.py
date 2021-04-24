from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/users/{user_id}")
def read_item(user_id: int, q: Optional[str] = None):
    return {"user_id": user_id, "q": q}


class User(BaseModel):
    name: str
    dateOfBirth: str
    is_current: Optional[bool] = None


@app.put("/users/{user_id}")
def update_item(user_id: int, user: User):
    return {"user_name": user.name, "item_id": user_id}


class SocialMedia(BaseModel):
    name: str
    date: str


@app.post("/medias")
def social_media(phrase: str, media: SocialMedia):
    return {"social_media": media.name,
            "phrase": phrase,
            "date": media.date}