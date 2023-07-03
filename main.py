from fastapi import FastAPI
from routes.transaction_router import transaction_router
from routes.reference import reference_router

app = FastAPI(title="Bookkeeping API")

app.include_router(transaction_router)
app.include_router(reference_router)
