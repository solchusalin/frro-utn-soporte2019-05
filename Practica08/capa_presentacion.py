from tkinter import *
from tkinter import ttk
from capa_negocio import Perfumeria
import tkinter.messagebox as mbox
from tablas import Base, Articulo, Proveedor, Venta, Compra, LineaVenta, LineaCompra

class PresentacionNegocio:

    def __init__(self, window, cp):             #menu principal
        self.cp = cp
        self.window = window
        self.window.resizable(0, 1)
        self.window.title("D&D Perfumeria y Complementos")
        self.window.geometry("795x700")
        self.photo = PhotoImage(file="dyd.png")
        Label(window, image=self.photo).place(relwidth=1, relheight=1)
        Button(window, text='Articulos', fg="blue", font=("arial", 14), borderwidth=5, cursor = "hand2", relief = "raised", command=lambda: self.art()).grid(row=0, column=0, padx=5, pady=5)
        Button(window, text='Proveedores', fg="blue", font=("arial", 14), borderwidth=5, cursor = "hand2", relief = "raised", command=lambda: self.prov()).grid(row=1, column=0, padx=5, pady=5)
        Button(window, text='  Ventas  ', fg="blue", font=("arial", 14), borderwidth=5, cursor = "hand2", relief = "raised", command=lambda: self.venta()).grid(row=2, column=0, padx=5, pady=5)
        Button(window, text=' Compras ', fg="blue", font=("arial", 14), borderwidth=5, cursor = "hand2", relief = "raised", command=lambda: self.compra()).grid(row=3, column=0, padx=5, pady=5)

# ARTICULOS

    def art(self):              #ventana articulos
        self.winArt=Toplevel()
        self.winArt.transient(master=self.window)
        self.winArt.title("Articulos")
        Button(self.winArt, text='Agregar articulo', fg="blue", command=lambda: self.alta_art()).grid(row=0, column=0, padx=5, pady=5)
        Label(self.winArt, text='Ingrese codigo del articulo: ').grid(row=0, column=3, sticky=(E, E), padx=0, pady=5)
        self.cod = StringVar()
        icod = Entry(self.winArt, textvariable=self.cod).grid(row=0, column=4, sticky=(E, W), padx=3, pady=5)
        Button(self.winArt, text=' Buscar ', fg="blue", command=lambda: self.buscar_articulo()).grid(row=0, column=5, sticky=(W, W), padx=5, pady=5)

        self.tabla = ttk.Treeview(self.winArt, selectmode=BROWSE)
        self.tabla = ttk.Treeview(self.winArt, columns=(0,1,2,3,4))
        self.tabla.grid(row=3, column=0, sticky=(E, W), columnspan=6, padx=5, pady=5)
        self.tabla.heading('#0', text='Codigo', anchor=CENTER)
        self.tabla.heading('#1', text='Descripcion', anchor=CENTER)
        self.tabla.heading('#2', text='Precio Compra', anchor=CENTER)
        self.tabla.heading('#3', text='Precio Venta', anchor=CENTER)
        self.tabla.heading('#4', text='Stock', anchor=CENTER)
        self.tabla.heading('#5', text='Proveedor', anchor=CENTER)

        Button(self.winArt, text=' Eliminar ', fg="blue", command=lambda: self.baja_art()).grid(row=10, column=4, sticky=(E, E), padx=5, pady=5)
        Button(self.winArt, text='Modificar', fg="blue", command=lambda: self.modif_art()).grid(row=10, column=5, sticky=(W, W), padx=5, pady=5)
        Button(self.winArt, text=' Menu ', command=lambda: self.winArt.destroy()).grid(row=10, column=5, sticky=(E,E), padx=5, pady=5)
        self.get_art()

    def buscar_articulo(self):
        if self.cod.get() == '':
            self.get_art()
        else:
            registros = self.tabla.get_children()
            for r in registros:
                self.tabla.delete(r)
            art = self.cp.buscar_art(self.cod.get())
            self.tabla.insert("", 0, text=art.codigo, values=(art.desc, art.precio_com, art.precio_vta, art.stock_real, art.cuit_prov))

    def alta_art(self, art=None):
        self.winAlta=Toplevel()
        self.winAlta.transient(master=self.winArt)
        self.winAlta.title("Agregar articulo")

        Label(self.winAlta, text='Codigo:').grid(row=0, column=0, sticky=(E, W), padx=5, pady=5)
        Label(self.winAlta, text='Descripcion:').grid(row=1, column=0, sticky=(E, W), padx=5, pady=5)
        Label(self.winAlta, text='Precio Compra:').grid(row=2, column=0, sticky=(E, W), padx=5, pady=5)
        Label(self.winAlta, text='Precio Venta:').grid(row=3, column=0, sticky=(E, W), padx=5, pady=5)
        Label(self.winAlta, text='Proveedor:').grid(row=4, column=0, sticky=(E, W), padx=5, pady=5)

        self.codigo = IntVar(value=getattr(art, 'codigo', 0))
        self.desc = StringVar(value=getattr(art, 'desc', ''))
        self.precio_com = DoubleVar(value=getattr(art, 'precio_com', 0))
        self.precio_vta = DoubleVar(value=getattr(art, 'precio_vta', 0))
        self.cuit_prov = IntVar(value=getattr(art, 'cuit_prov', 0))

        Entry(self.winAlta, textvariable=self.codigo).grid(row=0, column=1, sticky=(E, W), padx=5, pady=5)
        Entry(self.winAlta, textvariable=self.desc).grid(row=1, column=1, sticky=(E, W), padx=5, pady=5)
        Entry(self.winAlta, textvariable=self.precio_com).grid(row=2, column=1, sticky=(E, W), padx=5, pady=5)
        Entry(self.winAlta, textvariable=self.precio_vta).grid(row=3, column=1, sticky=(E, W), padx=5, pady=5)
        Entry(self.winAlta, textvariable=self.cuit_prov).grid(row=4, column=1, sticky=(E, W), padx=5, pady=5)

        Button(self.winAlta, text="Aceptar", fg="blue", command=lambda: self.aceptarAltaArt()).grid(row=6, column=1, sticky=(W, W), padx=5, pady=5)
        Button(self.winAlta, text="Cancelar", command=lambda: self.winAlta.destroy()).grid(row=6, column=1, sticky=(E, E), padx=5)


    def aceptarAltaArt(self):
        alta = self.cp.alta_art(Articulo(codigo=self.codigo.get(), desc=self.desc.get(), precio_com=self.precio_com.get(), precio_vta=self.precio_vta.get(), stock_real=0, cuit_prov=self.cuit_prov.get()))
        if alta == 1:
            mbox.showinfo('Error alta', 'El proveedor ingresado no existe.')
        elif alta == 2:
            mbox.showinfo('Error alta', 'El codigo ingresado ya existe.')
        else:
            self.get_art()
            self.winAlta.destroy()
            mbox.showinfo('Alta exitosa', 'El articulo se agrego con exito.')

    def baja_art(self):
        art = self.tabla.focus()
        if art:
            baja = mbox.askyesno('Eliminar articulo', '¿Desea eliminar el articulo?', default='no', parent=self.winArt)
            if baja:
                cod = self.tabla.item(art, 'text')
                self.cp.baja_art(cod)
                self.get_art()

    def modif_art(self):
        item = self.tabla.focus()
        cod = self.tabla.item(item, 'text')
        art = self.cp.buscar_art(cod)
        if art:
            self.winMod=Toplevel()
            self.winMod.geometry("300x200")
            self.winMod.transient(master=self.winArt)
            self.winMod.title("Modificar articulo")

            Label(self.winMod, text='Codigo:').grid(row=1, column=0, sticky=(E, W), padx=5, pady=5)
            Label(self.winMod, text='Descripcion:').grid(row=2, column=0, sticky=(E, W), padx=5, pady=5)
            Label(self.winMod, text='Precio Compra:').grid(row=3, column=0, sticky=(E, W), padx=5, pady=5)
            Label(self.winMod, text='Precio Venta:').grid(row=4, column=0, sticky=(E, W), padx=5, pady=5)
            Label(self.winMod, text='Proveedor:').grid(row=5, column=0, sticky=(E, W), padx=5, pady=5)


            self.codigo = IntVar(value=getattr(art, 'codigo', art.codigo))
            self.desc = StringVar(value=getattr(art, 'desc', art.desc))
            self.precio_com = DoubleVar(value=getattr(art, 'precio_com', art.precio_com))
            self.precio_vta = DoubleVar(value=getattr(art, 'precio_vta', art.precio_vta))
            self.cuit_prov = IntVar(value=getattr(art, 'cuit_prov', art.cuit_prov))

            Label(self.winMod, textvariable=self.codigo).grid(row=1, column=1, sticky=W, padx=5, pady=5)
            Entry(self.winMod, textvariable=self.desc).grid(row=2, column=1, sticky=(E, W), padx=5, pady=5)
            Entry(self.winMod, textvariable=self.precio_com).grid(row=3, column=1, sticky=(E, W), padx=5, pady=5)
            Entry(self.winMod, textvariable=self.precio_vta).grid(row=4, column=1, sticky=(E, W), padx=5, pady=5)
            Label(self.winMod, textvariable=self.cuit_prov).grid(row=5, column=1, sticky=W, padx=5, pady=5)

            Button(self.winMod, text="Guardar", fg="blue", command=lambda: self.guardarModA()).grid(row=6, column=1, sticky=(W, W), padx=5, pady=5)
            Button(self.winMod, text="Cancelar", command=lambda: self.winMod.destroy()).grid(row=6, column=1, sticky=(E, E), padx=5)

            self.get_art()

    def guardarModA(self):
        self.cp.modificacion_art(Articulo(desc=self.desc.get(), precio_com=self.precio_com.get(), precio_vta=self.precio_vta.get()))
        self.get_art()
        self.winMod.destroy()

    def get_art(self):
        registros = self.tabla.get_children()
        for r in registros:
            self.tabla.delete(r)

        articulos = self.cp.todos_art()
        for a in articulos:
            self.tabla.insert("", 0, text=a.codigo, values=(a.desc, a.precio_com, a.precio_vta, a.stock_real, a.cuit_prov))

# PROVEEDORES

    def prov(self):             #ventana proveedores
        self.winProv=Toplevel()
        self.winProv.transient(master=window)
        self.winProv.title("Proveedores")
        Button(self.winProv, text='Agregar proveedor', fg="blue", command=lambda: self.alta_prov()).grid(row=0, column=0, padx=5, pady=5)
        Label(self.winProv, text='Ingrese cuit del proveedor: ').grid(row=0, column=3, sticky=(E, E), padx=0, pady=5)
        self.cuit = IntVar()
        icuit = Entry(self.winProv, textvariable=self.cuit).grid(row=0, column=4, sticky=(E, W), padx=3, pady=5)
        Button(self.winProv, text=' Buscar ', fg="blue", command=lambda: self.buscar_proveedor()).grid(row=0, column=5, sticky=(W, W), padx=5, pady=5)

        self.tabla = ttk.Treeview(self.winProv, selectmode=BROWSE)
        self.tabla = ttk.Treeview(self.winProv, columns=(0,1,2))
        self.tabla.grid(row=3, column=0, sticky=(E, W), columnspan=6, padx=5, pady=5)
        self.tabla.heading('#0', text='Cuit', anchor=CENTER)
        self.tabla.heading('#1', text='Razon Social', anchor=CENTER)
        self.tabla.heading('#2', text='Telefono', anchor=CENTER)
        self.tabla.heading('#3', text='Estado', anchor=CENTER)


        Button(self.winProv, text='Dar de baja', fg="blue", command=lambda: self.baja_prov()).grid(row=10, column=4, sticky=(E, E), padx=5, pady=5)
        Button(self.winProv, text='Modificar', command=lambda: self.modif_prov()).grid(row=10, column=5, sticky=(W, W), padx=5, pady=5)
        Button(self.winProv, text=' Menu ', command=lambda: self.winProv.destroy()).grid(row=10, column=5, sticky=(E,E), padx=5, pady=5)
        self.get_prov()

    def modif_prov(self):
        item = self.tabla.focus()
        cuit = self.tabla.item(item, 'text')
        prov = self.cp.buscar_prov(cuit)
        if prov:
            self.winMod=Toplevel()
            self.winMod.geometry("300x200")
            self.winMod.transient(master=self.winProv)
            self.winMod.title("Modificar proveedor")

            Label(self.winMod, text='Cuit:').grid(row=1, column=0, sticky=(E, W), padx=5, pady=5)
            Label(self.winMod, text='Razon Social:').grid(row=2, column=0, sticky=(E, W), padx=5, pady=5)
            Label(self.winMod, text='Telefono:').grid(row=3, column=0, sticky=(E, W), padx=5, pady=5)

            self.cuit = IntVar(value=getattr(prov, 'cuit', prov.cuit))
            self.razon_social = StringVar(value=getattr(prov, 'razon_social', prov.razon_social))
            self.telefono = IntVar(value=getattr(prov, 'telefono', prov.telefono))

            Label(self.winMod, textvariable=self.cuit).grid(row=1, column=1, sticky=W, padx=5, pady=5)
            Entry(self.winMod, textvariable=self.razon_social).grid(row=2, column=1, sticky=(E, W), padx=5, pady=5)
            Entry(self.winMod, textvariable=self.telefono).grid(row=3, column=1, sticky=(E, W), padx=5, pady=5)


            Button(self.winMod, text="Guardar", fg="blue", command=lambda: self.guardarModP()).grid(row=6, column=1, sticky=(W, W), padx=5, pady=5)
            Button(self.winMod, text="Cancelar", command=lambda: self.winMod.destroy()).grid(row=6, column=1, sticky=(E, E), padx=5)

            self.get_prov()

    def guardarModP(self):
        self.cp.modificacion_prov(Proveedor(razon_social=self.razon_social.get(), telefono=self.telefono.get()))
        self.get_prov()
        self.winMod.destroy()

    def alta_prov(self, prov=None):
        self.winAlta=Toplevel()
        self.winAlta.transient(master=self.winProv)
        self.winAlta.title("Agregar proveedor")

        Label(self.winAlta, text='Cuit:').grid(row=0, column=0, sticky=(E, W), padx=5, pady=5)
        Label(self.winAlta, text='Razon Social:').grid(row=1, column=0, sticky=(E, W), padx=5, pady=5)
        Label(self.winAlta, text='Telefono:').grid(row=2, column=0, sticky=(E, W), padx=5, pady=5)
        Label(self.winAlta, text='Estado:').grid(row=3, column=0, sticky=(E, W), padx=5, pady=5)

        self.cuit = IntVar(value=getattr(prov, 'cuit', 0))
        self.razon_social = StringVar(value=getattr(prov, 'razon_social', ''))
        self.telefono = IntVar(value=getattr(prov, 'telefono', 0))
        self.estado = StringVar(value=getattr(prov, 'estado', 'habilitado'))

        Entry(self.winAlta, textvariable=self.cuit).grid(row=0, column=1, sticky=(E, W), padx=5, pady=5)
        Entry(self.winAlta, textvariable=self.razon_social).grid(row=1, column=1, sticky=(E, W), padx=5, pady=5)
        Entry(self.winAlta, textvariable=self.telefono).grid(row=2, column=1, sticky=(E, W), padx=5, pady=5)
        Label(self.winAlta, textvariable=self.estado).grid(row=3, column=1, sticky=(W, W), padx=5, pady=5)


        Button(self.winAlta, text="Aceptar", fg="blue", command=lambda: self.aceptarAltaProv()).grid(row=6, column=1, sticky=(W, W), padx=5, pady=5)
        Button(self.winAlta, text="Cancelar", command=lambda: self.winAlta.destroy()).grid(row=6, column=1, sticky=(E, E), padx=5)

    def baja_prov(self):
        prov = self.tabla.focus()
        if prov:
            baja = mbox.askyesno('Baja proveedor', '¿Desea dar de baja al proveedor?', default='no', parent=self.winProv)
            if baja:
                cuit = self.tabla.item(prov, 'text')
                self.cp.baja_prov(cuit)
                self.get_prov()

    def aceptarAltaProv(self):
        p = self.cp.alta_prov(Proveedor(cuit=self.cuit.get(), razon_social=self.razon_social.get(), telefono=self.telefono.get(), estado="habilitado"))
        if p == 1:
            mbox.showinfo('Error alta', 'El cuit ingresado ya existe.')
        else:
            self.get_prov()
            self.winAlta.destroy()
            mbox.showinfo('Alta exitosa', 'El proveedor se agrego con exito.')

    def buscar_proveedor(self):
        if self.cuit.get() == 0:
            self.get_prov()
        else:
            registros = self.tabla.get_children()
            for r in registros:
                self.tabla.delete(r)
            prov = self.cp.buscar_prov(self.cuit.get())
            self.tabla.insert("", 0, text=prov.cuit, values=(prov.razon_social, prov.telefono, prov.estado))

    def get_prov(self):
        registros = self.tabla.get_children()
        for r in registros:
            self.tabla.delete(r)

        proveedores = self.cp.todos_prov()
        for p in proveedores:
            self.tabla.insert("", 0, text=p.cuit, values=(p.razon_social, p.telefono, p.estado))

# VENTAS

    def venta(self):            #ventana ventas
        self.winVta=Toplevel()
        self.winVta.transient(master=self.window)
        self.winVta.title("Ventas")
        Button(self.winVta, text='Agregar venta', fg="blue", command=lambda: self.alta_venta()).grid(row=0, column=0, padx=5, pady=5)
        Label(self.winVta, text='Ingrese fecha de venta: ').grid(row=0, column=3, sticky=(E, E), padx=0, pady=5)
        self.fecha = StringVar()
        ifecha = Entry(self.winVta, textvariable=self.fecha).grid(row=0, column=4, sticky=(E, W), padx=3, pady=5)
        Button(self.winVta, text=' Buscar ', fg="blue", command=lambda: self.buscar_venta()).grid(row=0, column=5, sticky=(W, W), padx=5, pady=5)

        self.tabla = ttk.Treeview(self.winVta, selectmode=BROWSE)
        self.tabla = ttk.Treeview(self.winVta, columns=(0,1))
        self.tabla.grid(row=3, column=0, sticky=(E, W), columnspan=6, padx=5, pady=5)
        self.tabla.heading('#0', text='Numero', anchor=CENTER)
        self.tabla.heading('#1', text='Fecha', anchor=CENTER)
        self.tabla.heading('#2', text='Precio Total', anchor=CENTER)

        Button(self.winVta, text='Ver detalles', fg="blue", command=lambda: self.get_lv()).grid(row=10, column=4, sticky=(W, W), padx=5, pady=5)
        Button(self.winVta, text=' Menu ', command=lambda: self.winVta.destroy()).grid(row=10, column=4, sticky=(E,E), padx=5, pady=5)
        self.get_ventas()

    def alta_venta(self, v=None):
        self.winAltaV=Toplevel()
        self.winAltaV.transient(master=self.winVta)
        self.winAltaV.title("Agregar venta")

        Label(self.winAltaV, text='Fecha: ').grid(row=0, column=0, sticky=(E, W), padx=5, pady=5)
        Label(self.winAltaV, text='(AAAA-MM-DD)', fg="grey").grid(row=1, column=0, sticky=(E, W))

        self.fecha = StringVar(value=getattr(v, 'fecha', '0000-00-00'))

        Entry(self.winAltaV, textvariable=self.fecha).grid(row=0, column=1, sticky=(E, W), padx=5, pady=5)

        Button(self.winAltaV, text="Siguiente", fg="blue", command=lambda: self.carga_lv()).grid(row=5, column=1, sticky=(W, W), padx=5, pady=5)
        Button(self.winAltaV, text="Crear", fg="blue", command=lambda: self.crear_vta()).grid(row=5, column=0, sticky=(W, W), padx=5, pady=5)
        Button(self.winAltaV, text="Cancelar", command=lambda: self.winAltaV.destroy()).grid(row=5, column=1, sticky=(E, E), padx=5, pady=5)

    def crear_vta(self):
        self.v = self.cp.alta_vta(Venta(fecha=self.fecha.get()))

    def carga_lv(self, lv=None):
        self.winAltaV.destroy()
        self.winAlta=Toplevel()
        self.winAlta.transient(master=self.winVta)
        self.winAlta.title("Agregar venta")

        Label(self.winAlta, text='Cod. Articulo:').grid(row=0, column=0, sticky=(E, W), padx=5, pady=5)
        Label(self.winAlta, text='Cantidad:').grid(row=1, column=0, sticky=(E, W), padx=5, pady=5)

        self.cod_art = IntVar(value=getattr(lv, 'cod_art', 0))
        self.cantidad = IntVar(value=getattr(lv, 'cantidad', ''))

        Entry(self.winAlta, textvariable=self.cod_art).grid(row=0, column=1, sticky=(E, W), padx=5, pady=5)
        Entry(self.winAlta, textvariable=self.cantidad).grid(row=1, column=1, sticky=(E, W), padx=5, pady=5)

        Button(self.winAlta, text="Buscar", command=lambda: self.artV_ok()).grid(row=0, column=2, sticky=(E, E), padx=5, pady=5)
        Button(self.winAlta, text="Agregar otro articulo", fg="blue", command=lambda: self.alta_lv()).grid(row=5, column=0, sticky=(W, W), padx=5, pady=5)
        Button(self.winAlta, text="Aceptar", fg="blue", command=lambda: self.aceptarAltaVta()).grid(row=5, column=1, sticky=(W, W), padx=5, pady=5)


    def buscar_venta(self):
        if self.fecha.get() == '':
            self.get_ventas()
        else:
            registros = self.tabla.get_children()
            for r in registros:
                self.tabla.delete(r)
            ventas = self.cp.buscar_vta(self.fecha.get())
            for v in ventas:
                self.tabla.insert("", 0, text=v.nro, values=(v.fecha, v.precio_total))


    def artV_ok(self):
        art = self.cp.buscar_art(self.cod_art.get())
        if art is None:
            mbox.showinfo('Error', 'El articulo ingresado no existe.')
        else:
            mbox.showinfo('Exito', 'Articulo encontrado.')

    def calcu_subtotV(self, cod, cant):
        a = self.cp.buscar_art(cod)
        subtot = a.precio_vta * cant
        return subtot

    def alta_lv(self):  #aca se crean las lineas venta
        lv = self.cp.alta_lineaV(LineaVenta(nro_vta=self.v.nro, cod_art=self.cod_art.get(), cantidad=self.cantidad.get(), subtotal=self.calcu_subtotV(self.cod_art.get(), self.cantidad.get())))
        if lv == 0:
            self.winAlta.destroy()
            self.carga_lv()
        else:
            mbox.showinfo('Alerta', 'Stock insuficiente')

    def aceptarAltaVta(self, total=0):
        lv = self.cp.alta_lineaV(LineaVenta(nro_vta=self.v.nro, cod_art=self.cod_art.get(), cantidad=self.cantidad.get(), subtotal=self.calcu_subtotV(self.cod_art.get(), self.cantidad.get())))
        if lv == 0:
            lineasv = self.cp.buscar_lv(self.v.nro)
            for lv in lineasv:
                total = total + lv.subtotal
            self.v.precio_total = total
            self.cp.modificacion_vta(self.v)
            self.get_ventas()
            self.winAlta.destroy()
            mbox.showinfo('Venta exitosa', 'La venta se registro con exito.')
        else:
            mbox.showinfo('Error', 'Stock insuficiente')


    def get_ventas(self):
        registros = self.tabla.get_children()
        for r in registros:
            self.tabla.delete(r)

        ventas = self.cp.todos_vta()
        for v in ventas:
            self.tabla.insert("", 0, text=v.nro, values=(v.fecha, v.precio_total))

    def get_lv(self):
        self.winLV=Toplevel()
        self.winLV.transient(master=self.winVta)
        self.winLV.title("Detalles de la compra")
        self.tablaLV = ttk.Treeview(self.winLV, selectmode=BROWSE)
        self.tablaLV = ttk.Treeview(self.winLV, columns=(0,1))
        self.tablaLV.grid(row=3, column=0, sticky=(E, W), columnspan=6, padx=5, pady=5)
        self.tablaLV.heading('#0', text='Cod. Articulo', anchor=CENTER)
        self.tablaLV.heading('#1', text='Cantidad', anchor=CENTER)
        self.tablaLV.heading('#2', text='Subtotal', anchor=CENTER)
        Button(self.winLV, text="Cerrar", command=lambda: self.winLV.destroy()).grid(row=5, column=5, sticky=(E, E), padx=5, pady=5)

        v = self.tabla.focus()
        if v:
            nro = self.tabla.item(v, 'text')
            lineasv = self.cp.buscar_lv(nro)
            for l in lineasv:
                self.tablaLV.insert("", 0, text=l.cod_art, values=(l.cantidad, l.subtotal))


# COMPRAS

    def compra(self):              #ventana compras
        self.winCom=Toplevel()
        self.winCom.transient(master=self.window)
        self.winCom.title("Compras")
        Button(self.winCom, text='Agregar compra', fg="blue", command=lambda: self.alta_compra()).grid(row=0, column=0, padx=5, pady=5)
        Label(self.winCom, text='Ingrese fecha de compra: ').grid(row=0, column=3, sticky=(E, E), padx=0, pady=5)
        self.fecha = StringVar()
        ifecha = Entry(self.winCom, textvariable=self.fecha).grid(row=0, column=4, sticky=(E, W), padx=3, pady=5)
        Button(self.winCom, text=' Buscar ', fg="blue", command=lambda: self.buscar_compra()).grid(row=0, column=5, sticky=(W, W), padx=5, pady=5)

        self.tabla = ttk.Treeview(self.winCom, selectmode=BROWSE)
        self.tabla = ttk.Treeview(self.winCom, columns=(0,1,2))
        self.tabla.grid(row=3, column=0, sticky=(E, W), columnspan=6, padx=5, pady=5)
        self.tabla.heading('#0', text='Numero', anchor=CENTER)
        self.tabla.heading('#1', text='Fecha', anchor=CENTER)
        self.tabla.heading('#2', text='Proveedor', anchor=CENTER)
        self.tabla.heading('#3', text='Precio Total', anchor=CENTER)

        Button(self.winCom, text='Ver detalles', fg="blue", command=lambda: self.get_lc()).grid(row=10, column=5, sticky=(W, W), padx=5, pady=5)
        Button(self.winCom, text=' Menu ', command=lambda: self.winCom.destroy()).grid(row=10, column=5, sticky=(E,E), padx=5, pady=5)
        self.get_compras()

    def buscar_compra(self):
        if self.fecha.get() == '':
            self.get_compras()
        else:
            registros = self.tabla.get_children()
            for r in registros:
                self.tabla.delete(r)
            compras = self.cp.buscar_com(self.fecha.get())
            for c in compras:
                self.tabla.insert("", 0, text=c.nro, values=(c.fecha, c.proveedor, c.precio_total))


    def alta_compra(self, c=None):
        self.winAltaC=Toplevel()
        self.winAltaC.transient(master=self.winCom)
        self.winAltaC.title("Agregar compra")

        Label(self.winAltaC, text='Fecha: ').grid(row=0, column=0, sticky=(E, W), padx=5, pady=5)
        Label(self.winAltaC, text='(AAAA-MM-DD HH:MM:SS)', fg="grey").grid(row=1, column=0, sticky=(E, W))
        Label(self.winAltaC, text='Proveedor: ').grid(row=2, column=0, sticky=(E, W), padx=5, pady=5)
        Label(self.winAltaC, text='(cuit)', fg="grey").grid(row=3, column=0, sticky=(E, W))

        self.fecha = StringVar(value=getattr(c, 'fecha', ''))
        self.proveedor = IntVar(value=getattr(c, 'proveedor', 0))

        Entry(self.winAltaC, textvariable=self.fecha).grid(row=0, column=1, sticky=(E, W), padx=5, pady=5)
        Entry(self.winAltaC, textvariable=self.proveedor).grid(row=2, column=1, sticky=(E, W), padx=5, pady=5)

        Button(self.winAltaC, text="Buscar", command=lambda: self.crear_com()).grid(row=2, column=2, sticky=(E, E), padx=5, pady=5)
        Button(self.winAltaC, text="Siguiente", fg="blue", command=lambda: self.carga_lc()).grid(row=5, column=1, sticky=(W, W), padx=5, pady=5)
        Button(self.winAltaC, text="Cancelar", command=lambda: self.winAltaC.destroy()).grid(row=5, column=1, sticky=(E, E), padx=5, pady=5)

    def crear_com(self):
        self.c = self.cp.alta_com(Compra(fecha=self.fecha.get(), proveedor=self.proveedor.get()))
        if self.c == 1:
            mbox.showinfo('Error', 'El proveedor ingresado no existe.')
        elif self.c == 2:
            mbox.showinfo('Error', 'El proveedor se encuentra inhabilitado.')
        else:
            mbox.showinfo('Exito', 'Proveedor encontrado.')


    def carga_lc(self, lc=None):
        self.winAltaC.destroy()
        self.winAlta=Toplevel()
        self.winAlta.transient(master=self.winCom)
        self.winAlta.title("Agregar compra")

        Label(self.winAlta, text='Cod. Articulo:').grid(row=0, column=0, sticky=(E, W), padx=5, pady=5)
        Label(self.winAlta, text='Cantidad:').grid(row=1, column=0, sticky=(E, W), padx=5, pady=5)
        #Label(self.winAlta, text='Subtotal:').grid(row=3, column=0, sticky=(E, W), padx=5, pady=5)

        self.cod_art = IntVar(value=getattr(lc, 'cod_art', 0))
        self.cantidad = IntVar(value=getattr(lc, 'cantidad', ''))
        self.subtotal = DoubleVar(value=getattr(lc, 'subtotal', 0))

        Entry(self.winAlta, textvariable=self.cod_art).grid(row=0, column=1, sticky=(E, W), padx=5, pady=5)
        Entry(self.winAlta, textvariable=self.cantidad).grid(row=1, column=1, sticky=(E, W), padx=5, pady=5)

        Button(self.winAlta, text="Buscar", command=lambda: self.art_ok()).grid(row=0, column=2, sticky=(E, E), padx=5, pady=5)
        Button(self.winAlta, text="Agregar otro articulo", fg="blue", command=lambda: self.alta_lc()).grid(row=5, column=0, sticky=(W, W), padx=5, pady=5)
        Button(self.winAlta, text="Aceptar", fg="blue", command=lambda: self.aceptarAltaCom()).grid(row=5, column=1, sticky=(W, W), padx=5, pady=5)

    def art_ok(self):
        art = self.cp.buscar_art(self.cod_art.get())
        if art is None:
            mbox.showinfo('Error', 'El articulo ingresado no existe.')
        elif art.cuit_prov != self.proveedor.get():
            mbox.showinfo('Error', 'El articulo no pertenece al proveedor ingresado.')
        else:
            mbox.showinfo('Exito', 'Articulo encontrado.')

    def calcu_subtotC(self, cod, cant):
        a = self.cp.buscar_art(cod)
        subtot = a.precio_com * cant
        return subtot


    def alta_lc(self):  #aca se crean las lineas compra
        lc = self.cp.alta_lineaC(LineaCompra(nro_com=self.c.nro, cod_art=self.cod_art.get(), cantidad=self.cantidad.get(), subtotal=self.calcu_subtotC(self.cod_art.get(), self.cantidad.get())))
        self.winAlta.destroy()
        self.carga_lc()


    def aceptarAltaCom(self, total=0):
        lc = self.cp.alta_lineaC(LineaCompra(nro_com=self.c.nro, cod_art=self.cod_art.get(), cantidad=self.cantidad.get(), subtotal=self.calcu_subtotC(self.cod_art.get(), self.cantidad.get())))
        lineasc = self.cp.buscar_lc(self.c.nro)
        for lc in lineasc:
            total = total + lc.subtotal
        self.c.precio_total = total
        self.cp.modificacion_com(self.c)
        self.get_compras()
        self.winAlta.destroy()
        mbox.showinfo('Compra exitosa', 'La compra se registro con exito.')


    def get_compras(self):
        registros = self.tabla.get_children()
        for r in registros:
            self.tabla.delete(r)

        compras = self.cp.todos_com()
        for c in compras:
            self.tabla.insert("", 0, text=c.nro, values=(c.fecha, c.proveedor, c.precio_total))

    def get_lc(self):
        self.winLC=Toplevel()
        self.winLC.transient(master=self.winCom)
        self.winLC.title("Detalles de la compra")
        self.tablaLC = ttk.Treeview(self.winLC, selectmode=BROWSE)
        self.tablaLC = ttk.Treeview(self.winLC, columns=(0,1))
        self.tablaLC.grid(row=3, column=0, sticky=(E, W), columnspan=6, padx=5, pady=5)
        self.tablaLC.heading('#0', text='Cod. Articulo', anchor=CENTER)
        self.tablaLC.heading('#1', text='Cantidad', anchor=CENTER)
        self.tablaLC.heading('#2', text='Subtotal', anchor=CENTER)
        Button(self.winLC, text="Cerrar", command=lambda: self.winLC.destroy()).grid(row=5, column=5, sticky=(E, E), padx=5, pady=5)

        c = self.tabla.focus()
        if c:
            nro = self.tabla.item(c, 'text')
            lineasc = self.cp.buscar_lc(nro)
            for l in lineasc:
                self.tablaLC.insert("", 0, text=l.cod_art, values=(l.cantidad, l.subtotal))



if __name__ == '__main__':
    window = Tk()
    cp = Perfumeria()
    cpn = PresentacionNegocio(window, cp)
    window.mainloop()
