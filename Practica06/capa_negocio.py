from ejercicio01 import Socio
from ejercicio02 import DatosSocio


class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        return self.datos.buscar(id_socio)

    def buscar_dni(self, dni_socio):
        return self.datos.buscar_dni(dni_socio)

    def todos(self):
        return self.datos.todos()

    def alta(self, socio):
        try:
            if (self.regla_1(socio) == True) and (self.regla_2(socio) == True) and (self.regla_3() == True):
                self.datos.alta(socio)
                return True
        except Exception as ex:
            return False

    def baja(self, id_socio):
        return self.datos.baja(id_socio)

    def modificacion(self, socio):
        if (self.regla_2(socio) == True):
            try:
                return self.datos.modificacion(socio)
            except LongitudInvalida as ex:
                return False

    def regla_1(self, socio):
        s = self.datos.buscar_dni(socio.dni)
        if s is None:
            return True
        else:
            raise DniRepetido


    def regla_2(self, socio):
        if len(socio.nombre) >= self.MIN_CARACTERES and len(socio.nombre) <= self.MAX_CARACTERES:
            if len(socio.apellido) >= self.MIN_CARACTERES and len(socio.apellido) <= self.MAX_CARACTERES:
                return True
            else:
                raise LongitudInvalida
        else:
            raise LongitudInvalida


    def regla_3(self):
        if len(self.datos.todos()) < self.MAX_SOCIOS:
            return True
        else:
            raise MaximoAlcanzado
