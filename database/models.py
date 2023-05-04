from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from database.connection import Base

class Pokemon(Base):
    __tablename__ = "pokemon"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    classification = Column(String)
    name = Column(String)
    percentage_male = Column(Float)
    type1 = Column(String)
    type2 = Column(String)
    generation = Column(Integer)
    is_legendary = Column(Boolean)

    stats = relationship("Stats", backref="pokemon")

class Stats(Base):
    __tablename__ = "stats"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pokemon_id = Column(Integer, ForeignKey("pokemon.id") )
    attack = Column(Integer)
    defense = Column(Integer)
    height_m = Column(Float)
    hp = Column(Integer)
    speed = Column(Integer)
    weight_kg = Column(Float)
    
    #pokemon = relationship("Pokemon", back_populates="stats")