from fastapi import FastAPI, HTTPException
from project.models.user import User
from project.controller.user import c_get_user

app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    db_user = await c_get_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users")
async def create_user(user: User):
    #user
    print("post")
    return

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    print("put")
    return

@app.delete("/users/")
async def delete_user(user_id):
    print("delete")
    return