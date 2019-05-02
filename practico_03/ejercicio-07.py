# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

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

def verificarfecha(fecha):
    query = 'select max(fecha) from personaPeso'
    cursor.execute(query)
    resultado = cursor.fetchall()
    if (resultado[0][0]== None):
        return  True
    elif (resultado[0][0] > fecha.date):
        return False
    else:
        return True


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


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()

con.close()



