from project.db.config import db_config
from project.db.connection import PostgreeSQLConnection

db = PostgreeSQLConnection(
    dbname=db_config.database,
    user=db_config.user,
    password=db_config.password,
    host=db_config.host,
    port=db_config.port
)

async def c_get_user(user_id: int):
    db.connect()
    user = db.select_user(f"SELECT * FROM users WHERE id = {user_id}")
    return user
