# Implementar la funcion listar_pesos, que devuelva el historial de pesos para una persona dada.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).

# Debe devolver:
# - Lista de (fecha, peso), donde fecha esta representado por el siguiente formato: AAAA-MM-DD.
#   Ejemplo:
#   [
#       ('2018-01-01', 80),
#       ('2018-02-01', 85),
#       ('2018-03-01', 87),
#       ('2018-04-01', 84),
#       ('2018-05-01', 82),
#   ]
# - False en caso de no cumplir con alguna validacion.


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

def buscar_persona(id_persona):
    query = 'select * from persona where idPersona = %s'
    value = id_persona
    cursor.execute(query, value)
    resultado = cursor.fetchall()
    if resultado == []:
        return False


def agregar_peso(id_persona, fecha, peso):
    if buscar_persona(id_persona) == False:
        print('El id no existe, registro no encontrado')
    else:
        if verificarfecha(fecha) == False:
            print('Existe un registro con una fecha posterior a la ingresada')
        else:
            query = 'insert into personaPeso (fecha,peso,idPersona) values ( %s, %f, %i)'
            valores = (fecha,peso,id_persona)
            cursor.execute(query,valores)
            con.commit()
            print(cursor.rowcount, 'Registro cargado')

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper

def listar_pesos(id_persona):

    if (buscar_persona(id_persona)== False):
        return  False
    else:
        query = 'select fecha,peso from personaPeso where idPersona = %d'
        valor = id_persona
        cursor.execute(query,valor)
        resultado = cursor.fetchall()
        for i in resultado:
            r = (i[0].strftime('%Y-%m-%d'), i[1])
            lista.append(r)

        return lista
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    agregar_peso(id_juan, datetime.datetime(2018, 5, 1), 80)
    agregar_peso(id_juan, datetime.datetime(2018, 6, 1), 85)
    pesos_juan = listar_pesos(id_juan)
    pesos_esperados = [
        ('2018-05-01', 80),
        ('2018-06-01', 85),
    ]
    assert pesos_juan == pesos_esperados
    # id incorrecto
    assert listar_pesos(200) == False


if __name__ == '__main__':
    pruebas()

con.close()




