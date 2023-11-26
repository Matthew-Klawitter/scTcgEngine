from sqlalchemy.orm import Session

from models.tcg import CardSets, CardSet, Cards, Card


def create_card_set(card_set_model: CardSets, db: Session):
    card_set = CardSet(**card_set_model.model_dump())
    db.add(card_set)
    db.commit()
    db.refresh(card_set)
    return card_set


def get_all_card_sets(db: Session):
    card_sets = db.query(CardSet).all()
    return card_sets


def get_card_set(id: int, db: Session):
    card_set = db.query(CardSet).get(id)
    return card_set


def delete_card_set(id: int, db: Session):
    card_set = db.query(CardSet).get(id)
    if card_set is None:
        return card_set
    else:
        db.delete(card_set)
        db.commit()
    return card_set


def update_card_set(id: int, card_set_model: CardSets, db: Session):
    card_set = db.query(CardSet).get(id)
    if card_set is None:
        return card_set
    else:
        for var, value in vars(card_set_model).items():
            setattr(card_set, var, value) if value else None
        db.commit()
    db.refresh(card_set)
    return card_set


def create_card(card_model: Cards, db: Session):
    card = Card(**card_model.model_dump())
    db.add(card)
    db.commit()
    db.refresh(card)
    return card


def get_all_cards(db: Session):
    cards = db.query(Card).all()
    return cards


def get_card(id: int, db: Session):
    card = db.query(Card).get(id)
    return card


def delete_card(id: int, db: Session):
    card = db.query(Card).get(id)
    if card is None:
        return card
    else:
        db.delete(card)
        db.commit()
    return card


def update_card(id: int, card_model: Cards, db: Session):
    card = db.query(Card).get(id)
    if card is None:
        return card
    else:
        for var, value in vars(card_model).items():
            setattr(card, var, value) if value else None
        db.commit()
    db.refresh(card)
    return card