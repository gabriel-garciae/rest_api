from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    print("get")
    return

@app.post("/users")
async def create_user(user):
    print("post")
    return

@app.put("/users/{user_id}")
async def update_user(user_id: int, user):
    print("put")
    return

@app.delete("/users/")
async def delete_user(user_id):
    print("delete")
    return