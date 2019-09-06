from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mbox
from ejercicio01 import Socio
from capa_negocio import NegocioSocio

class PresentacionSocios:

    def __init__(self, window, cns):
        self.cns = cns
        self.window = window
        self.window.title("ABM Socios")
        self.window.marco = ttk.Frame(window, borderwidth=1, relief="raised", padding=(10,10))
        self.window.marco.grid(column=0, row=0, padx=5, pady=5, sticky=(N, S, E, W))

        #tabla
        self.tabla = ttk.Treeview(window, selectmode=BROWSE)
        self.tabla = ttk.Treeview(window, columns=(1,2,3))
        self.tabla.grid(row=0, column=0, sticky=(E, W), columnspan=6, padx=5, pady=5)
        self.tabla.heading('#0', text='Id', anchor=CENTER)
        self.tabla.heading('#1', text='Nombre', anchor=CENTER)
        self.tabla.heading('#2', text='Apellido', anchor=CENTER)
        self.tabla.heading('#3', text='DNI', anchor=CENTER)
        self.get_socios()


        #botones
        Button(window, text='Alta', command=lambda: self.altaSocio()).grid(row=1, column=0, sticky=(E, W), padx=5, pady=5)
        Button(window, text='Baja', command=lambda: self.bajaSocio()).grid(row=1, column=1, sticky=(E, W), padx=5, pady=5)
        Button(window, text='Modificacion', command=lambda: self.modificarSocio()).grid(row=1, column=2, sticky=(E, W), padx=5, pady=5)

    def get_socios(self):
        #limpiar tabla
        registros = self.tabla.get_children()
        for r in registros:
            self.tabla.delete(r)
        #mostrar socios
        socios = self.cns.todos()
        for s in socios:
            self.tabla.insert("", 0, text=s.id, values=(s.nombre, s.apellido, s.dni))

    def bajaSocio(self):
        socio = self.tabla.focus()
        if socio:
            baja = mbox.askyesno('Baja', '¿Desea dar de baja al socio?', default='no', parent=self.window)
            if baja:
                id = self.tabla.item(socio, 'text')
                self.cns.baja(id)
                self.get_socios()

    def altaSocio(self, socio=None):
        self.winAlta=Toplevel()
        self.winAlta.transient(master=window)
        self.winAlta.title("Alta")

        #Label(self.winAlta, text='Id:').grid(row=1, column=0, sticky=(E, W), padx=5, pady=5)
        Label(self.winAlta, text='Nombre:').grid(row=1, column=0, sticky=(E, W), padx=5, pady=5)
        Label(self.winAlta, text='Apellido:').grid(row=2, column=0, sticky=(E, W), padx=5, pady=5)
        Label(self.winAlta, text='DNI:').grid(row=3, column=0, sticky=(E, W), padx=5, pady=5)
        self.id = IntVar(value=getattr(socio, 'id', 0))
        self.nombre = StringVar(value=getattr(socio, 'nombre', ''))
        self.apellido = StringVar(value=getattr(socio, 'apellido', ''))
        self.dni = IntVar(value=getattr(socio, 'dni', 0))
        self.cns.alta(Socio(nombre=self.nombre.get(), apellido=self.apellido.get(), dni=self.dni.get()))

        Entry(self.winAlta, textvariable=self.nombre).grid(row=1, column=1, sticky=(E, W), padx=5, pady=5)
        Entry(self.winAlta, textvariable=self.apellido).grid(row=2, column=1, sticky=(E, W), padx=5, pady=5)
        Entry(self.winAlta, textvariable=self.dni).grid(row=3, column=1, sticky=(E, W), padx=5, pady=5)

        Button(self.winAlta, text="Aceptar", command=lambda: self.aceptarAlta()).grid(row=4, column=0, sticky=(E, W), padx=5, pady=5)
        Button(self.winAlta, text="Cancelar", command=lambda: self.winAlta.destroy()).grid(row=4, column=2, sticky=(E, W), padx=5)

        self.get_socios()

    def aceptarAlta(self):
        self.cns.alta(Socio(nombre=self.nombre.get(), apellido=self.apellido.get(), dni=self.dni.get()))
        self.get_socios()
        self.winAlta.destroy()

    def modificarSocio(self):
        item = self.tabla.focus()
        id = self.tabla.item(item, 'text')
        socio = self.cns.buscar(id)
        if socio:
            self.winMod=Toplevel()
            self.winMod.transient(master=window)
            self.winMod.title("Modificacion")

            Label(self.winMod, text='Id:').grid(row=1, column=0, sticky=(E, W), padx=5, pady=5)
            Label(self.winMod, text='Nombre:').grid(row=2, column=0, sticky=(E, W), padx=5, pady=5)
            Label(self.winMod, text='Apellido:').grid(row=3, column=0, sticky=(E, W), padx=5, pady=5)
            Label(self.winMod, text='DNI:').grid(row=4, column=0, sticky=(E, W), padx=5, pady=5)

            self.id = IntVar(value=getattr(socio, 'id', socio.id))
            self.nombre = StringVar(value=getattr(socio, 'nombre', socio.nombre))
            self.apellido = StringVar(value=getattr(socio, 'apellido', socio.apellido))
            self.dni = IntVar(value=getattr(socio, 'dni', socio.dni))

            Label(self.winMod, textvariable=self.id).grid(row=1, column=1, sticky=W, padx=5, pady=5)
            Entry(self.winMod, textvariable=self.nombre).grid(row=2, column=1, sticky=(E, W), padx=5, pady=5)
            Entry(self.winMod, textvariable=self.apellido).grid(row=3, column=1, sticky=(E, W), padx=5, pady=5)
            Entry(self.winMod, textvariable=self.dni).grid(row=4, column=1, sticky=(E, W), padx=5, pady=5)

            Button(self.winMod, text="Guardar", command=lambda: self.guardarMod()).grid(row=5, column=0, sticky=(E, W), padx=5, pady=5)
            Button(self.winMod, text="Cancelar", command=lambda: self.winMod.destroy()).grid(row=5, column=2, sticky=(E, W), padx=5)

            self.get_socios()

    def guardarMod(self):
        self.cns.modificacion(Socio(id=self.id.get(), nombre= self.nombre.get(),apellido= self.apellido.get(),dni= self.dni.get()))
        self.get_socios()
        self.winMod.destroy()


if __name__ == '__main__':
    window = Tk()
    cns = NegocioSocio()
    cps = PresentacionSocios(window, cns)
    window.mainloop()




