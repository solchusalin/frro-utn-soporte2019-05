#Crear un Formulario que usando el control Treeview muestre una lista con los nombres de
#Ciudades Argentinas y su código postal (por lo menos 5 ciudades).

import tkinter
from tkinter import ttk


class Aplicacion(ttk.Frame):

    def __init__(self, ventana):
        super().__init__(ventana)
        ventana.title("Ciudades")
        self.marco=ttk.Frame(self, borderwidth=4, relief="ridge", padding=(15,15))
        self.tree = ttk.Treeview(self.marco, columns=('Ciudad', 'Código Postal'))
        self.tree.heading('#0', text='Id Ciudad')
        self.tree.heading('#1', text='Ciudad')
        self.tree.heading('#2', text='Código Postal')
        self.tree.column('#0', stretch=tkinter.YES)
        self.tree.column('#1', stretch=tkinter.YES)
        self.tree.column('#2', stretch=tkinter.YES)
        self.treeview = self.tree
        self.insert_data()
        self.marco.grid(column=0, row=0, padx=5, pady=5, sticky='nsew')
        self.treeview.grid(row=4, columnspan=3, sticky='nsew')
        self.pack()


    def insert_data(self):
        ciudades = ['Capitan Bermudez','Rosario', 'Buenos Aires', 'San Lorenzo', 'Cordoba','Salta']
        codigos = ['2154','2000', '1000', '2200', '5284','4400']
        for i in range(0, 6):
            self.treeview.insert('', 'end', text=i+1, values=(ciudades[i], codigos[i]))



def main():
    ventana = tkinter.Tk()
    app = Aplicacion(ventana)
    app.mainloop()


if __name__ == '__main__':
    main()
