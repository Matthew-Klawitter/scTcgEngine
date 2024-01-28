from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT

from controllers.tcg.tcg_controller import create_card_set, get_all_card_sets, get_card_set, delete_card_set, \
    update_card_set
from database import get_db
from models.tcg.tcg import CardSets


router = APIRouter(
    prefix="/tcg/card_set",
    dependencies=[Depends(get_db)]
)


@router.post("/")
def create(card_set_model: CardSets, db: Session = Depends(get_db)):
    card_set = create_card_set(card_set_model, db)
    return card_set


@router.get("/")
def get(db: Session = Depends(get_db)):
    card_sets = get_all_card_sets(db)
    return card_sets


@router.get("/{id}")
def get(id: int, db: Session = Depends(get_db)):
    card_set = get_card_set(id, db)
    if card_set is None:
        raise HTTPException(status_code=404, detail=f"Card Set with id {id} does not exist")
    else:
        return card_set


@router.delete("/delete/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    card_set = delete_card_set(id, db)
    if card_set is None:
        raise HTTPException(status_code=404, detail=f"Card Set with id {id} does not exist")
    return Response(status_code=HTTP_204_NO_CONTENT)


@router.put("/update/{id}")
def update(id: int, card_set_model: CardSets, db: Session = Depends(get_db)):
    card_set = update_card_set(id, card_set_model, db)
    if card_set is None:
        raise HTTPException(status_code=404, detail=f"Card Set with id {id} does not exist")
    return card_set