from sqlalchemy import collumn, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Estudante(Base):
    