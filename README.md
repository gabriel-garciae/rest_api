# FastAPI

## What is FastAPI?

**FastAPI** is a modern, fast, and high-performance web framework for building APIs in Python. It was developed by Sebastián Ramírez and is based on modern Python patterns such as:

- **Type hints** (type annotations)
- **Pydantic** for data validation
- **Starlette** for asynchronous web functionality
- **OpenAPI** (Swagger) for automatic documentation

### Key features of FastAPI

- **Performance**: One of the fastest Python APIs available
- **Fast development**: Cleaner code and fewer bugs
- **Automatic documentation**: Generates interactive documentation automatically
- **Automatic validation**: Runtime type and data validation
- **Python 3.6+**: Full support for modern Python features
- **Asynchronous**: Native async/await support

---

## Project structure

```
project/
├── __init__.py
├── controller/          # Business logic
│   ├── __init__.py
│   └── user.py         # User controllers
├── db/                  # Database layer
│   ├── __init__.py
│   ├── config.py       # Database configurations
│   ├── connection.py   # PostgreSQL connection
│   └── ddl.sql         # Table creation scripts
├── models/              # Data models
│   ├── __init__.py
│   ├── body_post.json  # Request examples
│   └── user.py         # User Pydantic model
└── routes/              # API route definitions
    ├── __init__.py
    └── user.py         # API endpoints
```

---

## 🛣️ Routes (Endpoints) - The heart of the API

### What are routes?

Routes are the **paths** that your API exposes to the external world. They define how clients can interact with your application through different HTTP methods.

### Main HTTP methods

| Method | Description | Usage |
|--------|-------------|-------|
| `GET` | **Read** data | Fetch information |
| `POST` | **Create** new data | Add new records |
| `PUT` | **Update** existing data | Modify complete records |
| `DELETE` | **Remove** data | Delete records |

### Practical example of project routes

```python
# GET - Find user by ID
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    # Logic to find user
    pass

# POST - Create new user
@app.post("/users")
async def create_user(user: User):
    # Logic to create user
    pass

# PUT - Update existing user
@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    # Logic to update user
    pass

# DELETE - Remove user
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    # Logic to delete user
    pass
```

### How routes work

1. **Decorator `@app.get()`**: Defines the HTTP method and path
2. **Route parameters**: `{user_id}` are dynamic parameters
3. **Async function**: `async def` allows non-blocking operations
4. **Return**: The function returns data or an HTTP response

---

## Dependencies - FastAPI's injection system

### What are dependencies?

Dependencies are **functions or classes** that FastAPI automatically executes before calling your route function. They are used for:

- **Data validation**
- **Authentication** and authorization
- **Database connections**
- **Logging** and monitoring
- **Cache** and optimizations

### Types of dependencies

#### 1. **Function dependencies**
```python
from fastapi import Depends

def get_db():
    db = PostgreeSQLConnection(...)
    try:
        yield db
    finally:
        db.close()

@app.get("/users/{user_id}")
async def get_user(user_id: int, db: PostgreeSQLConnection = Depends(get_db)):
    # db is automatically injected
    user = db.select_user(f"SELECT * FROM users WHERE id = {user_id}")
    return user
```

#### 2. **Class dependencies**
```python
from fastapi import Depends

class DatabaseService:
    def __init__(self, db: PostgreeSQLConnection = Depends(get_db)):
        self.db = db
    
    def get_user(self, user_id: int):
        return self.db.select_user(f"SELECT * FROM users WHERE id = {user_id}")

@app.get("/users/{user_id}")
async def get_user(user_id: int, db_service: DatabaseService = Depends()):
    return db_service.get_user(user_id)
```

#### 3. **Dependencies with parameters**
```python
def verify_token(token: str = Header(...)):
    if not token:
        raise HTTPException(status_code=401, detail="Token required")
    return token

@app.get("/users/{user_id}")
async def get_user(
    user_id: int, 
    token: str = Depends(verify_token)
):
    # Token is automatically validated
    pass
```

---

## Database - PostgreSQL

### Configuration
```python
# project/db/config.py
class DatabaseConfig:
    def __init__(self):
        self.host = os.getenv('DB_HOST', 'localhost')
        self.port = int(os.getenv('DB_PORT', '5432'))
        self.database = os.getenv('DB_NAME', 'rest_api_db')
        self.user = os.getenv('DB_USER', 'postgres')
        self.password = os.getenv('DB_PASSWORD', 'postgres123')
```

### Environment variables
Create a `.env` file in the project root:
```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=rest_api_db
DB_USER=postgres
DB_PASSWORD=your_password_here
```

---

## How to run the project

### 1. **Install dependencies**
```bash
# Using Poetry (recommended)
poetry install

# Or using pip
pip install -r requirements.txt
```

### 2. **Configure database**

#### Option A: Local PostgreSQL
```bash
# Create PostgreSQL database
createdb rest_api_db

# Run DDL scripts
psql -d rest_api_db -f project/db/ddl.sql
```

#### Option B: Using Docker (Recommended)
```bash
# Start PostgreSQL using docker-compose
docker-compose up -d

# The database will be automatically initialized with the schema
# from init.sql/init.sql

# To stop the database
docker-compose down

# To view logs
docker-compose logs postgres

# To restart the database
docker-compose restart postgres
```

### 3. **Run the application**
```bash
# Using Poetry
poetry run uvicorn project.routes.user:app --reload

# Or directly
uvicorn project.routes.user:app --reload
```

### 4. **Access documentation**
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## API usage examples

### Create user
```bash
curl -X POST "http://localhost:8000/users" \
     -H "Content-Type: application/json" \
     -d '{
       "id": 1,
       "nome": "John Silva",
       "empresa": "TechCorp",
       "cargo": "Developer",
       "anos_experiencia": 5,
       "salario": 8000.00,
       "qualidade_servico": "Excellent"
     }'
```

### Get user
```bash
curl -X GET "http://localhost:8000/users/1"
```

### Update user
```bash
curl -X PUT "http://localhost:8000/users/1" \
     -H "Content-Type: application/json" \
     -d '{
       "id": 1,
       "nome": "John Silva",
       "empresa": "TechCorp",
       "cargo": "Senior Developer",
       "anos_experiencia": 6,
       "salario": 9000.00,
       "qualidade_servico": "Excellent"
     }'
```

### Delete user
```bash
curl -X DELETE "http://localhost:8000/users/1"
```

---

## Testing the API

### 1. **Automated tests**
```bash
# Install pytest
pip install pytest pytest-asyncio

# Run tests
pytest
```

### 2. **Manual testing**
- Use **Swagger UI** at `/docs`
- Use **Postman** or **Insomnia**
- Use **curl** in terminal

---

## Debugging and logs

### Development logs
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    logger.info(f"Looking for user with ID: {user_id}")
    # ... rest of code
```

### Debug mode
```bash
uvicorn project.routes.user:app --reload --log-level debug
```

---

## Additional resources

### Official documentation
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [Uvicorn Documentation](https://www.uvicorn.org/)

### Recommended tutorials
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [SQLAlchemy + FastAPI](https://fastapi.tiangolo.com/tutorial/sql-databases/)
- [Authentication & Security](https://fastapi.tiangolo.com/tutorial/security/)

---

## Author

**Gabriel Evangelista**
- Email: eng.gabrielgevangelista@gmail.com
- GitHub: [gabriel-garciae](https://github.com/gabriel-garciae)

---

## Conclusion

This project demonstrates a complete implementation of a REST API using FastAPI, with:

- ✅ **Clean architecture** and organization
- ✅ **Automatic data validation** with Pydantic
- ✅ **Automatic documentation** with Swagger
- ✅ **PostgreSQL connection** for persistence
- ✅ **Complete CRUD operations**
- ✅ **Proper error handling**

FastAPI is an excellent choice for developing modern, fast, and scalable APIs in Python! 🚀