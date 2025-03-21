from fastapi import FastAPI
from pydantic import BaseModel
from typing import 

app = FastAPI()

class User(BaseModel):
    id: int
    username: str
    email: str