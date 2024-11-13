from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define a Pydantic model for the user data (request body)
class User(BaseModel):
    name: str
    age: int

# Define a Pydantic model for the user response
class UserResponse(BaseModel):
    name: str
    age: int

# In-memory storage for users
users = {}

@app.get("/greet/{username}")
async def greet_user(username: str):
    return {"message": f"Hello, {username}!"}

@app.post("/users/", response_model=List[UserResponse])  # Corrected response_model here
async def create_users(user_list: List[User]):
    responses = []
    for user in user_list:
        users[user.name] = user.age
        responses.append(UserResponse(name=user.name, age=user.age))
    return responses

@app.get("/users/{username}", response_model=UserResponse)  # Corrected response_model here
async def get_user(username: str):
    age = users.get(username)
    if age is not None:
        return UserResponse(name=username, age=age)
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{username}", response_model=UserResponse)  # Corrected response_model here
async def update_user(username: str, user: User):
    if username in users:
        users[username] = user.age
        return UserResponse(name=username, age=user.age)
    else:
        raise HTTPException(status_code=404, detail="User not found")
