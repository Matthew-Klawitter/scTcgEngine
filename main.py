from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT

from controllers.tcg_controller import update_card_set, delete_card_set, get_card_set, get_all_card_sets, \
    create_card_set, update_card, delete_card, get_card, get_all_cards, create_card
from database import get_db
from models.tcg import CardSets, Cards

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/tcg/card_set")
def create(card_set_model: CardSets, db: Session = Depends(get_db)):
    card_set = create_card_set(card_set_model, db)
    return card_set


@app.get("/tcg/card_set")
def get(db: Session = Depends(get_db)):
    card_sets = get_all_card_sets(db)
    return card_sets


@app.get("/tcg/card_set/{id}")
def get(id: int, db: Session = Depends(get_db)):
    card_set = get_card_set(id, db)
    if card_set is None:
        raise HTTPException(status_code=404, detail=f"Card Set with id {id} does not exist")
    else:
        return card_set


@app.delete("/tcg/card_set/delete/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    card_set = delete_card_set(id, db)
    if card_set is None:
        raise HTTPException(status_code=404, detail=f"Card Set with id {id} does not exist")
    return Response(status_code=HTTP_204_NO_CONTENT)


@app.put("/tcg/card_set/update/{id}")
def update(id: int, card_set_model: CardSets, db: Session = Depends(get_db)):
    card_set = update_card_set(id, card_set_model, db)
    if card_set is None:
        raise HTTPException(status_code=404, detail=f"Card Set with id {id} does not exist")
    return card_set


@app.post("/tcg/card")
def create(card_model: Cards, db: Session = Depends(get_db)):
    card = create_card(card_model, db)
    return card


@app.get("/tcg/card")
def get(db: Session = Depends(get_db)):
    cards = get_all_cards(db)
    return cards


@app.get("/tcg/card/{id}")
def get(id: int, db: Session = Depends(get_db)):
    card = get_card(id, db)
    if card is None:
        raise HTTPException(status_code=404, detail=f"Card with id {id} does not exist")
    else:
        return card


@app.delete("/tcg/card/delete/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    card = delete_card(id, db)
    if card is None:
        raise HTTPException(status_code=404, detail=f"Card with id {id} does not exist")
    return Response(status_code=HTTP_204_NO_CONTENT)


@app.put("/tcg/card/update/{id}")
def update(id: int, card_model: Cards, db: Session = Depends(get_db)):
    card = update_card(id, card_model, db)
    if card is None:
        raise HTTPException(status_code=404, detail=f"Card with id {id} does not exist")
    return card