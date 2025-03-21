from fastapi import FastAPI
from pydantic import BaseModel
from typing import List 
import uvicorn

app = FastAPI()

class User(BaseModel):
    id: int
    username: str
    email: str

users = [
    User(id=1, username="user1", email="user1@example.com"),
    User(id=2, username="user2", email="user2@example.com"),
    User(id=3, username="user3", email="user3@example.com")
]

@app.get("/users", response_model=List[User])
def get_users():
    return users
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return {"error": "User not found"}


@app.post("/create_user", response_model=User)
def create_user(user: User):
    users.append(user)
    return user

@app.put("/update_user/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    for i, user in enumerate(users):
        if user.id == user_id:
            users[i] = updated_user
            return updated_user
    return {"error": "User not found"}

@app.delete("/delete_user/{user_id}")
def delete_user(user_id: int):
    for i, user in enumerate(users):
        if user.id == user_id:
            del users[i]
            return {"message": "User deleted"}
    return {"error": "User not found"}


if __name__ == "__main__":

