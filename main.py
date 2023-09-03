from fastapi import FastAPI

from routes import transaction_router
from routes import reference_router
from routes import auth_router
from routes import user_router

app = FastAPI(title="Bookkeeping API")

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(transaction_router)
app.include_router(reference_router)
