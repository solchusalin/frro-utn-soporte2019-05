# Implementar un modelo Socio a traves de Alchemy que cuente con los siguientes campos:
# - id_socio: entero (clave primaria, auto-incremental, unico)
# - dni: entero (unico)
# - nombre: string (longitud 250)
# - apellido: string (longitud 250)

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Socio(Base):
    __tablename__ = 'socios'
    id_socio = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    dni_socio = Column(Integer, unique=True)
    nombre = Column(String(250))
    apellido = Column(String(250))

engine = create_engine('mysql://root:root@localhost:3306/soporte-practica03')
Base.metadata.bind = engine
db_session = sessionmaker()
db_session.bind = engine
session = db_session()

Base.metadata.create_all(engine)




