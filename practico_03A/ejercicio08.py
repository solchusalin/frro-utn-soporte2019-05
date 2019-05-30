from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio01 import buscaPersona

Base = declarative_base()

engine = create_engine('mysql://root:root@localhost:3306/soporte-practica03')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def listar_pesos(idPers):
    personas=[]
    if(buscaPersona(idPers) == False):
        print('El id no se encuentra')
        return False
    else:
        pesos = session.query(PersonaPeso).filter_by(persona_id=idPers).all()
        for p in pesos:
            perpeso = (p.fechaRegistro.strftime("%Y-%m-%d"), p.peso)
            personas.append(perpeso)
            return personas

lista=listar_pesos(2)
for l in lista:
    print (l.fechaRegistro, l.peso)
