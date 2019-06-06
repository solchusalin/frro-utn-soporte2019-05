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


def borraPersona(id):
    pers = session.query(Persona)
    for p in pers:
        if p.idPersona == id:
            session.delete(p)
            session.commit()
            rta = True
        else:
            rta = False
    return rta

borraPersona(3)
