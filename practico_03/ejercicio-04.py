# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import  pymysql

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


def buscar_persona(id_persona):
    query = 'select * from persona where idPersona = %s'
    value = id_persona
    cursor.execute(query, value)
    resultado = cursor.fetchall()
    if resultado == []:
        return False
    else:
        return resultado[0]



# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper


@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()


con.close()
