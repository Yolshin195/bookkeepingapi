from fastapi import FastAPI, Depends

app = FastAPI(
    title="Bookkeeping API"
)


@app.get('/')
def hello():
    return 'Hello, world!'
