from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, VARCHAR
from sqlalchemy import create_engine

engine = create_engine('mysql://root:root@localhost:3306/soporte-practica03')
Base = declarative_base()
Base.metadata.bind = engine


class Socio(Base):
    __tablename__ = 'socios'
    id = Column(INTEGER, primary_key=True, autoincrement=True, unique=True)
    dni = Column(INTEGER, unique=True)
    nombre = Column(VARCHAR(250))
    apellido = Column(VARCHAR(250))

def crear_tabla():
    Base.metadata.create_all(engine)

crear_tabla()
