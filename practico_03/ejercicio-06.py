# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

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


def borrar_tabla_peso():
    query = 'drop table personaPeso'
    cursor.execute(query)
    con.commit()

def crear_tabla_peso():
    query = 'create table if not exists personaPeso(idPeso int not null auto increment primary key, fecha date, peso float (5,2), ' \
            'foreing key (idPersona) references persona(idPersona))'
    cursor.execute(query)

def borrar_tabla_peso():
    query = 'drop table personaPeso'
    cursor.execute(query)


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper


con.close()



