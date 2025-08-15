from src.db.connection import PostgreeSQLConnection

db = PostgreeSQLConnection(dbname="postgres", user="myuser", password="mypassword")

async def c_get_user(user_id: int):
    db.connect()
    user = db.excecute_query(f"SELECT * FROM users WHERE id = {user_id}")
    return user
