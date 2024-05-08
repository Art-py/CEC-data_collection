from fastapi import FastAPI

from services.api.test_model.router import test_model_router

app = FastAPI(title="CEC-data-collection")


app.include_router(test_model_router)
