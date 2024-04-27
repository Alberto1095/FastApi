from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models import Candidato
from dbSettings import SessionLocal

router = APIRouter()


def getDb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class CandidatoPostData(BaseModel):
    dni: str
    nombre: str
    apellido: str


@router.post("/candidato")
def createCandidato(candidato: CandidatoPostData, db: Session = Depends(getDb)):
    try:
        # Validar el DNI
        Candidato().validate_dni('dni', candidato.dni)
        # Crear el candidato e insertarlo en la base de datos
        db_candidato = Candidato(**candidato.model_dump())
        db.add(db_candidato)
        db.commit()
        db.refresh(db_candidato)
        return {"message": "Candidato creado."}
    except ValueError as e:
        raise HTTPException(
            status_code=400, detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="Error al crear el candidato."
        )
