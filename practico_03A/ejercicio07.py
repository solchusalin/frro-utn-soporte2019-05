from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio01 import buscaPersona
from ejercicio06 import PersonaPeso

Base = declarative_base()

engine = create_engine('mysql://root:root@localhost:3306/soporte-practica03')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def agregar_peso(idPers, fecha, peso):
    if(buscaPersona(idPers) == False):
        print('El id no se encuentra')
        return False
    else:
        pesos = session.query(PersonaPeso).filter_by(persona_id=idPers).all()
        for p in pesos:
            if p.fechaRegistro >= fecha:
                return False
    pe = PersonaPeso()
    pe.fechaRegistro = fecha
    pe.peso = peso
    pe.persona_id = idPers
    session.commit()
    return pe.id

agregar_peso(3, datetime.datetime(2019,05,30), 60)
