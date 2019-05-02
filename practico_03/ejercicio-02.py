# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime
import pymysql

con = pymysql.connect(host='localhost',
                              port= 3306,
                              user='root',
                              password='julinob',
                              database='soporte_practica_03'
                              )

cursor = con.cursor()


def agregar_persona(nombre, nacimiento, dni, altura):
    query = 'insert into persona(nombre,fechaNacimiento,dni,altura) values (%s, %s, %s, %s)'
    values = (nombre,nacimiento,dni,altura)
    cursor.execute(query, values)
    con.commit()
    con.close()

    return cursor.lastrowid

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()

