from fastapi import FastAPI

app = FastAPI(
    title="Bookkeeping API"
)

fake_users = [
    {"id": 1, "role": "admin", "name": "Aleksey"}
]

fake_account = [
    {"id": 1, "name": "$"}
]

fake_operations = [
    {"id": 1}
]


@app.get('/')
def hello():
    return 'Hello, world!'
