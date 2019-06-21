# Implementar los metodos de la capa de datos de socios.


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio01 import Base, Socio


class DatosSocio(object):

    def __init__(self):
        engine = create_engine('mysql://root:root@localhost:3306/soporte-practica03')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()

    def buscar(self, id):
        socios = self.session.query(Socio).all()
        for s in socios:
            if s.id_socio == id:
                return s               #rtype: Socio
        else:
            return None

    def buscar_dni(self, dni):
        socios = self.session
        for s in socios:
            if s.dni_socio == dni:
                return s            #rtype: Socio
        else:
            return None



    def todos(self):
        socios= self.session.query(Socio).all()
        return socios        #rtype: list

    def borrar_todos(self):
        socios = self.todos()
        for s in socios:
            self.session.delete(s)
        self.session.commit()
        if len(socios):
            return False    #lista no vacia
        else:
            return True     #lista vacia

    def alta(self, socio):
        self.session.add(socio)
        self.session.commit()
        return socio

    def baja(self, id):
        s = self.session.query(Socio).filter_by(id_socio=id).first()
        if s.id_socio == id:
            self.session.delete(s)
            self.session.commit()
            return True
        else:
            return False

    def modificacion(self, socio):
        self.session.commit()
        return socio


def pruebas():
    # alta
    datos = DatosSocio()
    socio = datos.alta(Socio(dni_socio=12345678, nombre='Juan', apellido='Perez'))
    assert socio.id > 0

    # baja
    assert datos.baja(socio.id_socio) == True

    # buscar
    socio_2 = datos.alta(Socio(dni_socio=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar(socio_2.id_socio) == socio_2

    # buscar dni
    socio_2 = datos.alta(Socio(dni_socio=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar(socio_2.dni_socio) == socio_2

    # modificacion
    socio_3 = datos.alta(Socio(dni_socio=12345680, nombre='Susana', apellido='Gimenez'))
    socio_3.nombre = 'Moria'
    socio_3.apellido = 'Casan'
    socio_3.dni_socio = 13264587
    datos.modificacion(socio_3)
    socio_3_modificado = datos.buscar(socio_3.id_socio)
    assert socio_3_modificado.id == socio_3.id_socio
    assert socio_3_modificado.nombre == 'Moria'
    assert socio_3_modificado.apellido == 'Casan'
    assert socio_3_modificado.dni_socio == 13264587

    # todos
    assert len(datos.todos()) == 2

    # borrar todos
    datos.borrar_todos()
    assert len(datos.todos()) == 0


if __name__ == '__main__':
    pruebas()
