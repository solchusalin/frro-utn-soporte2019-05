# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import pymysql

con = pymysql.connect(host='localhost',
                              port= 3306,
                              user='root',
                              password='julinob',
                              database='soporte_practica_03'
                              )
cursor = con.cursor()


def crear_tabla():
    query = 'create table if not exists persona(idPersona int not null auto_increment primary key,' \
            'nombre varchar(30),' \
            'fechaNacimiento date,dni int,altura float(3,2))'

    cursor.execute(query)
    con.commit()

def borrar_tabla():
    query = 'drop table persona'
    cursor.execute(query)
    con.commit()

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper

con.close()
