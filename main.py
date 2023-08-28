from fastapi import FastAPI

import db
from routes import transaction_router
from routes import reference_router
from routes import auth_router

app = FastAPI(title="Bookkeeping API")

app.include_router(auth_router)
app.include_router(transaction_router)
app.include_router(reference_router)
