from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from ejercicio01 import Persona

Base = declarative_base()

class PersonaPeso(Base):
    __tablename__ = 'personaPeso'
    id = Column(Integer, primary_key=True, autoincrement=True)
    persona_id = Column(Integer, ForeignKey(Persona.idPersona))
    fechaRegistro = Column(DateTime)
    peso = Column(Integer)
    persona = relationship(Persona)

engine = create_engine('mysql://root:root@localhost:3306/soporte-practica03')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def crearTablaPeso ():
    Base.metadata.create_all(engine)

crearTablaPeso()




