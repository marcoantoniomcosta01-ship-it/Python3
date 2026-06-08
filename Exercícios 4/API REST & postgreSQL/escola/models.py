# models.py
from sqlalchemy import Column, Integer, String
from database import Base

class Estudante(Base):
    __tablename__ = "estudantes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    idade = Column(Integer)

class Professores(Base):
    __tablename__ = 'professores'