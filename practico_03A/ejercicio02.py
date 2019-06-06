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

def agregar_persona(nombre, nacimiento, dni, altura):
    p = Persona()
    p.nombre = nombre
    p.fechaNacimiento = nacimiento
    p.dni = dni
    p.altura = altura
    session.add(p)
    session.commit()
    return p.idPersona

print(agregar_persona('maria sol salin', datetime.datetima(1997,02,19), 40115115, 170))
print(agregar_persona('juliana della ceca', datetime.datetime(1996, 03, 13), 39125740, 165))
print(agregar_persona('juan perez', datetime.datetime(1994, 04, 01), 39155560, 185))
