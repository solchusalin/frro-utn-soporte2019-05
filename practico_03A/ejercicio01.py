from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Persona(Base):
    __tablename__ = 'persona'
    idPersona = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(250), nullable=False)
    fechaNacimiento = Column (Date)
    dni = Column(Integer, unique=True)
    altura= Column(Integer)

engine = create_engine('mysql://root:root@localhost:3306/soporte-practica03')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def creaTabla():
    Base.metadata.create_all(engine)

def borraTabla():
    Persona.__table__.drop()


creaTabla()

#borraTabla()
