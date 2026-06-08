# schemas.py
from pydantic import BaseModel

class EstudanteBase(BaseModel):
    nome: str
    idade: int


class EstudanteCreate(EstudanteBase):
    pass


class EstudanteOut(EstudanteBase):
    id: int

    class Config:
        orm_mode = True