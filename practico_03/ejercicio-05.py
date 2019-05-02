# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

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

def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    if(buscar_persona(id_persona) == False):
        print('El id no se encuentra')
    else:
        print('Registro actual:',buscar_persona(id_persona))
        query = 'update persona set nombre = %s, fechaNacimiento = %s, dni = %d, altura = %f where idPersona = %d'
        values =(nombre,nacimiento,dni,altura,id_persona)
        cursor.execute(query,values)
        con.commit()
        print(cursor.rowcount, 'Regristro actualizado exitosamente')
        if cursor.rowcount == 0:
            return False
        else:
            return True

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
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()


con.close()



