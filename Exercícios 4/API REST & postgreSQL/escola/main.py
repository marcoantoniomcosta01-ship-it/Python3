# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import SessionLocal

app = FastAPI()


# Dependência para abrir e fechar sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/estudantes/{estudante_id}", response_model=schemas.EstudanteOut)
def ler_estudantes(estudante_id: int, db: Session = Depends(get_db)):
    
    estudante = db.query(models.Estudante).filter(
        models.Estudante.id == estudante_id
    ).first()

    if estudante is None:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")

    return estudante

@app.post("/estudantes", response_model=schemas.EstudanteOut)
def criar_estudante(estudante: schemas.EstudanteCreate, db: Session = Depends(get_db)):
    novo_estudante = models.Estudante(
        nome=estudante.nome,
        idade=estudante.idade
    )
    db.add(novo_estudante)
    db.commit()
    db.refresh(novo_estudante)
    return novo_estudante
