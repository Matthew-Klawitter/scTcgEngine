import enum

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base

CARD_SET_TABLE_NAME = "SC_TCG_CARD_SET"
CARD_TABLE_NAME = "SC_TCG_CARD"


class Rarity(enum.Enum):
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    LEGENDARY = 4


class CardSet(Base):
    __tablename__ = CARD_SET_TABLE_NAME

    id = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(String)
    cards = relationship("Card", backref="card_set")


class CardSets(BaseModel):
    name: str
    desc: str


class Card(Base):
    __tablename__ = CARD_TABLE_NAME

    id = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(String)
    rarity = Column(Enum(Rarity))
    card_set_id = Column(Integer, ForeignKey(CARD_SET_TABLE_NAME + ".id"))


class Cards(BaseModel):
    name: str
    desc: str
    rarity: int
    card_set_id: int
