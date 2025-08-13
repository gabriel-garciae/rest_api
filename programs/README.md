# API Client and Provider Examples

Simple examples demonstrating API architecture concepts.

## API Provider (`program_festapi.py`)

```python
from fastapi import FastAPI
import random

servidor = FastAPI()

@servidor.get("/recursos")
def numero_aleatorio():
    num = random.randint(1, 100)
    return num
```

**What it does:**
- Creates a FastAPI server
- Exposes GET endpoint at `/recursos`
- Returns random number 1-100

## API Client (`client.py`)

```python
import requests

url = "http://localhost:8000/recursos"
response = requests.get(url)

print(response.status_code)
print(response.json())
```

**What it does:**
- Makes HTTP GET request to the API
- Displays status code and response data

## How to Run

**Install dependencies:**
```bash
pip install requests fastapi uvicorn
```

**Start server:**
```bash
uvicorn program_festapi:servidor --reload --host 0.0.0.0 --port 8000
```

**Test client:**
```bash
python client.py
```

## Key Concepts

- **API Provider**: Exposes endpoints, handles requests, returns data
- **API Client**: Consumes endpoints, makes requests, processes responses
- **HTTP Communication**: GET requests, status codes, JSON responses

## Data Flow

```
Client Request → Server generates number → JSON Response → Client displays result
``` 