from pydantic import BaseModel, validator

class Stats(BaseModel):
    id: int
    pokemon_id: int
    attack: int
    defense: int
    height_m: float
    speed: int
    weight_kg: float

    class Config:
        orm_mode = True

class Pokemon(BaseModel):
    id: int
    classification: str
    name: str
    percentage_male: float
    type1: str
    type2: str
    generation: int
    is_legendary: bool
    stats: Stats

    class Config:
        orm_mode = True

