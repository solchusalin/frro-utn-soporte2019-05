from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio04 import buscaPersona

Base = declarative_base()

engine = create_engine('mysql://root:root@localhost:3306/soporte-practica03')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def actualizaPersona(id, nombre, fecha, dni, altura):
    if(buscaPersona(id) == False):
        print('El id no se encuentra')
        return False
    else:
        print('Registro actual:', buscaPersona(id))
        pers = session.query(Persona)
        for p in pers:
            if p.idPersona == id:
                p.nombre=nombre
                p.fechaNacimiento=fecha
                p.dni=dni
                p.altura=altura
                break
        session.commit()
        return True

actualizaPersona(2,'sol martinez', datetime.datetime(1997, 02, 11), 40400400, 160)
