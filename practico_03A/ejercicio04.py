from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio01 import Persona

Base = declarative_base()

engine = create_engine('mysql://root:root@localhost:3306/soporte-practica03')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def buscaPersona(id):
    pers = session.query(Persona)
    for p in pers:
        if p.idPersona == id:
            return (p.idPersona, p.nombre, p.fechaNacimiento, p.dni, p.altura)
        else:
            return False

assert(buscaPersona(5)==False)
