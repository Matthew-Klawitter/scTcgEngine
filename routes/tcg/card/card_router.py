from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT

from controllers.tcg.tcg_controller import create_card, get_all_cards, get_card, delete_card, update_card
from database import get_db
from models.tcg.tcg import Cards


router = APIRouter(
    prefix="/tcg/card",
    dependencies=[Depends(get_db)]
)


@router.post("/")
def create(card_model: Cards, db: Session = Depends(get_db)):
    card = create_card(card_model, db)
    return card


@router.get("/")
def get(db: Session = Depends(get_db)):
    cards = get_all_cards(db)
    return cards


@router.get("/{id}")
def get(id: int, db: Session = Depends(get_db)):
    card = get_card(id, db)
    if card is None:
        raise HTTPException(status_code=404, detail=f"Card with id {id} does not exist")
    else:
        return card


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    card = delete_card(id, db)
    if card is None:
        raise HTTPException(status_code=404, detail=f"Card with id {id} does not exist")
    return Response(status_code=HTTP_204_NO_CONTENT)


@router.put("/{id}")
def update(id: int, card_model: Cards, db: Session = Depends(get_db)):
    card = update_card(id, card_model, db)
    if card is None:
        raise HTTPException(status_code=404, detail=f"Card with id {id} does not exist")
    return card
