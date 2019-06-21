#Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
#y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter
#que le corresponde (como se ve imagen) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada.

from tkinter import *
from tkinter import messagebox

class Calculadora:

    def Borrar(self):
        self.rec.delete(0, END)


    def Accion(self, num):
        self.rec.insert(END, num)


    def Igual(self):
        try:
            self.igual = self.rec.get()
            self.equal =  eval(self.igual)
            self.rec.delete(0, END)
            self.rec.insert(END, self.equal)
        except ZeroDivisionError:
            messagebox.showinfo("Mensaje", "Error: División por cero")
            self.rec.delete(0, END)
        except SyntaxError or NameError:
            messagebox.showinfo("Mensaje", "Error: Datos inválidos")



    def __init__(self, calcu):
        calcu.title("Calculadora")
        calcu.geometry("310x250")
        self.rec = Entry(calcu, width=25,justify ='center')
        self.rec.grid(row=0, column=0, columnspan=4, pady=5)
        self.rec.focus_set()


calcu = Tk()
objeto = Calculadora(calcu)


botonCero = Button(calcu, text="0", width=7, height=2,bd=3,command=lambda: objeto.Accion(0))
botonUno = Button(calcu, text="1", width=7, height=2,bd=3,command=lambda: objeto.Accion(1))
botonDos = Button(calcu, text="2", width=7, height=2,bd=3,command=lambda: objeto.Accion(2))
botonTres = Button(calcu, text="3", width=7, height=2,bd=3,command=lambda: objeto.Accion(3))
botonCuatro = Button(calcu, text="4", width=7, height=2,bd=3,command=lambda: objeto.Accion(4))
botonCinco = Button(calcu, text="5", width=7, height=2,bd=3,command=lambda: objeto.Accion(5))
botonSeis = Button(calcu, text="6", width=7, height=2,bd=3,command=lambda: objeto.Accion(6))
botonSiete = Button(calcu, text="7", width=7, height=2,bd=3,command=lambda: objeto.Accion(7))
botonOcho = Button(calcu, text="8", width=7, height=2,bd=3,command=lambda: objeto.Accion(8))
botonNueve = Button(calcu, text="9", width=7, height=2,bd=3,command=lambda: objeto.Accion(9))
botonSuma = Button(calcu, text="+", width=7, height=2,bd=3,command=lambda: objeto.Accion('+'))
botonResta = Button(calcu, text="-", width=7, height=2,bd=3,command=lambda: objeto.Accion('-'))
botonMultiplicacion = Button(calcu, text="x", width=7, height=2,bd=3, command=lambda: objeto.Accion('*'))
botonDivision = Button(calcu, text="/", width=7, height=2,bd=3,command=lambda: objeto.Accion('/'))
botonIgual = Button(calcu, text="=", width=7, height=2,bd=3,command=objeto.Igual)
botonBorrar = Button(calcu, text="AC", width=7, height=2,bg='red',bd=3,command=objeto.Borrar)
botonSiete.grid(column=0, row=1)
botonOcho.grid(column=1, row=1)
botonNueve.grid(column=2, row=1)
botonCuatro.grid(column=0, row=2)
botonCinco.grid(column=1, row=2)
botonSeis.grid(column=2, row=2)
botonUno.grid(column=0, row=3)
botonDos.grid(column=1, row=3)
botonTres.grid(column=2, row=3)
botonCero.grid(column=0,row=4)
botonSuma.grid(column=4, row=2)
botonResta.grid(column=5, row=2)
botonMultiplicacion.grid(column=4, row=3)
botonDivision.grid(column=5, row=3)
botonIgual.grid(column=1, row=4)
botonBorrar.grid(column=2, row=4)

calcu.mainloop()
