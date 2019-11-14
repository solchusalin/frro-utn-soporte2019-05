from capa_datos import DatosArticulo, DatosProveedor, DatosVenta, DatosCompra, DatosLineaVenta, DatosLineaCompra

class StockInsuficiente(Exception):
    pass

class CuitRepetido(Exception):
    pass

class CodigoRepetido(Exception):
    pass

class Perfumeria(object):

    STOCK_MINIMO = 5


    def __init__(self):
        self.datosArt = DatosArticulo()
        self.datosProv = DatosProveedor()
        self.datosVta = DatosVenta()
        self.datosCom = DatosCompra()
        self.datosLV = DatosLineaVenta()
        self.datosLC = DatosLineaCompra()

# REGLAS

    def regla_1(self, cant, a):           #verificar en alta venta
        if a.stock_real >= (cant + self.STOCK_MINIMO):
            return True
        else:
            raise StockInsuficiente

    def regla_2(self, prov):
        p = self.buscar_prov(prov.cuit)
        if p is None:
            return True
        else:
            raise CuitRepetido

    def regla_3(self, art):
        a = self.buscar_art(art.codigo)
        if a is None:
            return True
        else:
            raise CodigoRepetido

# METODOS COMPRA

    def alta_com(self, com):
        p = self.buscar_prov(com.proveedor)
        if p is None:
            return 1
        elif p.estado == 'habilitado':
            self.datosCom.alta(com)
            return com
        else:
            return 2

    def todos_com(self):
        return self.datosCom.todos()

    def modificacion_com(self, com):
        return self.datosCom.modificacion(com)

    def buscar_com(self, fecha):
        return self.datosCom.buscar(fecha)

# METODOS LINEA COMPRA

    def alta_lineaC(self, lc):
        a = self.buscar_art(lc.cod_art)
        if a is None:
            return 1
        else:
            self.datosLC.alta(lc)
            a.stock_real = a.stock_real + lc.cantidad
            self.datosArt.modificacion(a)
            return 0

    def buscar_lc(self, num):
        return self.datosLC.buscar(num)

# METODOS VENTA

    def alta_vta(self, vta):
        return self.datosVta.alta(vta)

    def todos_vta(self):
        return self.datosVta.todos()

    def modificacion_vta(self, vta):
        return self.datosVta.modificacion(vta)

    def buscar_vta(self, fecha):
        return self.datosVta.buscar(fecha)

# METODOS LINEA VENTA

    def alta_lineaV(self, lv):
        art = self.buscar_art(lv.cod_art)
        if art is None:
            return 1
        try:
            if (self.regla_1(lv.cantidad, art) == True):
                self.datosLV.alta(lv)
                art.stock_real = art.stock_real - lv.cantidad
                self.datosArt.modificacion(art)
                return 0
        except Exception as ex:
            return 2

    def buscar_lv(self, num):
        return self.datosLV.buscar(num)

# METODOS ARTICULO

    def buscar_art(self, cod):
        return self.datosArt.buscar(cod)

    def todos_art(self):
        return self.datosArt.todos()

    def alta_art(self, art):
        p = self.buscar_prov(art.cuit_prov)
        if p is None:
            return 1
        try:
            if (self.regla_3(art) == True):
                self.datosArt.alta(art)
                return 0
        except Exception as ex:
            return 2


    def baja_art(self, cod):
        return self.datosArt.baja(cod)

    def modificacion_art(self, art):
        return self.datosArt.modificacion(art)

# METODOS PROVEEDOR

    def buscar_prov(self, cuit):
        return self.datosProv.buscar(cuit)

    def todos_prov(self):
        return self.datosProv.todos()

    def alta_prov(self, prov):
        try:
            if (self.regla_2(prov) == True):
                self.datosProv.alta(prov)
                return 0
        except Exception as ex:
            return 1

    def baja_prov(self, cuit):
        return self.datosProv.baja(cuit)

    def modificacion_prov(self, prov):
        return self.datosProv.modificacion(prov)
