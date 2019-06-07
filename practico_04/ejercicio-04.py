#Al Formulario del Ejercicio 3,  agregue  los siguientes botones
# 1- un  botón  Alta que inicia otra ventana donde puedo ingresar una ciudad y su código postal.
# 2- un botón Baja que borra del listado de ciudades la ciudad que esta selecionada en Treeview.
# 3- un botón Modificar.
#Todos los cambios se deben ver reflejados en la lista que se muestra.

import tkinter
from tkinter import *
from tkinter import ttk


def Alta():
    root = tkinter.Tk()
    root.title('Nueva Ciudad')
    root.marco = ttk.Frame(root, borderwidth=3, relief='ridge', padding=(15,15))
    root.marco.grid(column=0, row=0, padx=6, pady=6, sticky='nsew')
    root.ciudad = StringVar()
    root.codigo = StringVar()
    root.labCiudad = Label(root.marco, text='Ciudad:',bg='grey')
    root.labCodigo = Label(root.marco, text='Código Postal:', bg='grey')
    root.enCiudad = ttk.Entry(root.marco, textvariable=root.ciudad)
    root.enCodigo = ttk.Entry(root.marco, textvariable=root.codigo)
    root.botonAceptar = ttk.Button(root.marco, text='Aceptar',command=lambda: CargarDatos(root))
    root.labCiudad.grid(column=0, row=1, sticky='ew', padx=6, pady=6)
    root.labCodigo.grid(column=0, row=2, sticky='ew', padx=6, pady=6)
    root.enCiudad.grid(column=1, row=1, sticky='ew', padx=6, pady=6)
    root.enCodigo.grid(column=1, row=2, sticky='ew', padx=6, pady=6)
    root.botonAceptar.grid(column=1, row=3, sticky='ew', padx=6, pady=6)
    root.mainloop()


def CargarDatos(root):
    app.treeview.insert('', 'end', text=root.enCiudad.get(), values=root.enCodigo.get())
    root.destroy()

def Baja():
    i = app.treeview.focus()
    app.treeview.delete(i)


def Modificar():
    root = tkinter.Tk()
    root.title('Modificar Código Postal')
    root.marco = ttk.Frame(root, borderwidth=3, relief='raised', padding=(15,15))
    root.marco.grid(column=0, row=0, padx=6, pady=6, sticky='nsew')
    root.codigo = StringVar()
    root.labCodigo = Label(root.marco, text='Codigo Postal:', bg='grey')
    root.enCodigo = ttk.Entry(root.marco, textvariable=root.codigo)
    root.botonAceptar = ttk.Button(root.marco, text='Aceptar', command=lambda: Editar(root))
    root.labCodigo.grid(column=0, row=1, sticky='ew', padx=6, pady=6)
    root.enCodigo.grid(column=1, row=1, sticky='ew', padx=6, pady=6)
    root.botonAceptar.grid(column=1, row=2, sticky='ew', padx=6, pady=6)
    root.mainloop()


def Editar(root):
    i = app.treeview.focus()
    app.treeview.item(i, values=root.enCodigo.get())
    root.destroy()


def Datos(treeview):
       ciudades = ['Capitan Bermudez','Rosario', 'Buenos Aires', 'San Lorenzo', 'Cordoba','Salta']
       codigos = ['2154','2000', '1000', '2200', '5284','4400']
       for i in range(0, 6):
            treeview.insert('', 'end', text=ciudades[i], values=codigos[i])


app = tkinter.Tk()
app.title('Ciudades')
app.marco = ttk.Frame(app, borderwidth=2, relief='raised', padding=(10,10))
app.marco.grid(column=0, row=0, padx=6, pady=6, sticky='nsew')
app.treeview = ttk.Treeview(app.marco, selectmode=tkinter.BROWSE)
app.treeview = ttk.Treeview(app.marco, columns='#1')
app.treeview.heading("#0", text='Ciudad')
app.treeview.heading('#1', text='Código Postal')
Datos(app.treeview)
app.botonAlta=Button(app.marco, text='Alta', command=Alta)
app.botonBaja=Button(app.marco, text='Baja', command=Baja)
app.botonModificar=Button(app.marco, text='Modificar', command=Modificar)
app.treeview.grid(column=0, row=0, sticky="ew",columnspan=3, padx=6, pady=6)
app.botonAlta.grid(column=0, row=1, sticky="ew", padx=6, pady=6)
app.botonBaja.grid(column=1, row=1, sticky="ew", padx=6, pady=6)
app.botonModificar.grid(column=2, row=1, sticky="ew", padx=6, pady=6)
app.mainloop()


