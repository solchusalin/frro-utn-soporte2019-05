#Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
#y 4 botones de operaciones para las operaciones respectivas + , - , * , /
#al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 .

from tkinter import *
from tkinter import messagebox



def Suma():
    valor1 = float(entrada1.get())
    valor2 = float(entrada2.get())
    res = valor1 + valor2
    messagebox.showinfo("Mensaje", "El resultado  de la suma es: %.2f" %res)
    entrada1.delete(0, END)
    entrada2.delete(0, END)


def Resta():
    valor1 = float(entrada1.get())
    valor2 = float(entrada2.get())
    res = valor1 - valor2
    messagebox.showinfo("Mensaje", "El resultado de la resta es: %.2f" %res)
    entrada1.delete(0, END)
    entrada2.delete(0, END)


def Multiplicacion():
    valor1 = float(entrada1.get())
    valor2 = float(entrada2.get())
    res = valor1 * valor2
    messagebox.showinfo("Mensaje", "El resultado de la multiplicacion es: %.2f" %res)
    entrada1.delete(0, END)
    entrada2.delete(0, END)


def Division():
    valor1 = float(entrada1.get())
    valor2 = float(entrada2.get())
    try:
        res = valor1 / valor2
    except ZeroDivisionError:
        messagebox.showinfo("Mensaje", "Error división por cero")
    else:
        messagebox.showinfo("Mensaje", "El resultado de la divison es: %.2f" %res)
    finally:
        entrada1.delete(0, END)
        entrada2.delete(0, END)



calcu = Tk()
calcu.geometry("285x250")
calcu.title('Calculadora')
valor1 = StringVar()
valor1.set('Valor del Número 1')
label1 = Label(calcu, textvariable=valor1, height=2, foreground='blue')
label1.place(x=20, y=25)
numero1 = StringVar()
entrada1 = Entry(calcu, bd=4, textvariable=numero1)
entrada1.place(x=20, y=55)
valor2 = StringVar()
valor2.set('Valor del Número 2')
label2 = Label(calcu, textvariable=valor2, height=2, foreground='blue')
label2.place(x=20, y=115)
numero2 = StringVar()
entrada2 = Entry(calcu, bd=4, textvariable=numero2)
entrada2.place(x=20, y=145)
bt1 = Button(calcu, text="+",foreground= 'blue', command=Suma, width=5)
bt1.place(x=180, y=80)
bt2 = Button(calcu, text="-",foreground= 'blue', command=Resta, width=5)
bt2.place(x=230, y=80)
bt3 = Button(calcu, text="*",foreground= 'blue', command=Multiplicacion, width=5)
bt3.place(x=180, y=110)
bt4 = Button(calcu, text="/",foreground= 'blue', command=Division, width=5)
bt4.place(x=230, y=110)
calcu.mainloop()
