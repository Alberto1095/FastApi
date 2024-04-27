import re
from sqlalchemy import Column, String, TypeDecorator
from sqlalchemy.orm import validates
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Candidato(Base):
    __tablename__ = "candidatos"

    dni = Column(String, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)

    # validador para el DNI con el formato correcto
    @validates('dni')
    def validate_dni(self, key, value):
        if not re.match(r'^\d{8}[A-Za-z]$', value):
            raise ValueError('Formato DNI no valido')
        return value
