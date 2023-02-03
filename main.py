from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com",
    "http://127.0.0.1:5500",
    "http://localhost",
    "http://localhost:8080",
]

app = FastAPI(
    title="Trading App"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fake_users = [
    {'id': 1, "role": "admin", "name": "Bob"},
    {'id': 2, "role": "investor", "name": "Sam"},
    {'id': 3, "role": "trader", "name": "Sixer"}
]

# @app.get('/')
# def home():
#     return "API Tests!"

@app.get('/users')
def get_all_users():
    return fake_users

@app.get('/users/{user_id}')
def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 100, "amount": 2.12},
    {"id": 2, "user_id": 2, "currency": "BTC", "side": "sell", "price": 120, "amount": 2.12}
]

@app.get('/trades')
def get_trades(limit: int = 1, offset: int = 1):
    return fake_trades[offset:][:limit]

fake_users2 = [
    {'id': 1, "role": "admin", "name": "Bob"},
    {'id': 2, "role": "investor", "name": "Sam"},
    {'id': 3, "role": "trader", "name": "Sixer"}
]

@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_users2))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}