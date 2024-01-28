from fastapi import FastAPI

from routes.tcg.card import card_router
from routes.tcg.card_set import card_set_router

app = FastAPI()

app.include_router(card_router.router)
app.include_router(card_set_router.router)
