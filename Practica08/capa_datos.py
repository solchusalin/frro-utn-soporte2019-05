from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from tablas import Base, Articulo, Proveedor, Venta, Compra, LineaVenta, LineaCompra


class DatosArticulo(object):

    def __init__(self):
        engine = create_engine('mysql://root:root@localhost:3306/soporte-practico08')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()

    def buscar(self, cod):
        art = self.session.query(Articulo).filter_by(codigo=cod).first()
        return art

    def todos(self):
        articulos = self.session.query(Articulo).all()
        return articulos

    def alta(self, art):
        self.session.add(art)
        self.session.commit()
        return art

    def baja(self, cod_art):
        art = self.buscar(cod_art)
        if art is None:
            return False
        else:
            self.session.delete(art)
            self.session.commit()
            return True

    def modificacion(self, art):
        art = self.buscar(art.codigo)
        if art is None:
            return False
        else:
            self.session.query(Articulo).filter_by(codigo=art.codigo).update({Articulo.desc:art.desc, Articulo.precio_com:art.precio_com, Articulo.precio_vta:art.precio_vta, Articulo.stock_real:art.stock_real})
            self.session.commit()
        return True

class DatosProveedor(object):

    def __init__(self):
        engine = create_engine('mysql://root:root@localhost:3306/soporte-practico08')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()

    def buscar(self, cuit_prov):
        prov = self.session.query(Proveedor).filter_by(cuit=cuit_prov).first()
        return prov

    def todos(self):
        proveedores = self.session.query(Proveedor).all()
        return proveedores

    def alta(self, prov):
        self.session.add(prov)
        self.session.commit()
        return prov

    def baja(self, cuit_prov):
        prov = self.buscar(cuit_prov)
        if prov == None:
            return False
        else:
            self.session.query(Proveedor).filter_by(cuit=cuit_prov).update({Proveedor.estado:'inhabilitado'})
            self.session.commit()
            return True

    def modificacion(self, prov):
        self.session.query(Proveedor).filter_by(cuit=prov.cuit).update({Proveedor.razon_social:prov.razon_social, Proveedor.telefono:prov.telefono})
        self.session.commit()
        return True

class DatosVenta(object):

    def __init__(self):
        engine = create_engine('mysql://root:root@localhost:3306/soporte-practico08')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()

    def buscar(self, fecha):
        ventas = self.session.query(Venta).filter_by(fecha=fecha).all()
        return ventas

    def todos(self):
        ventas = self.session.query(Venta).all()
        return ventas

    def alta(self, vta):
        self.session.add(vta)
        self.session.commit()
        return vta

    def modificacion(self, vta):
        vta = self.session.query(Venta).filter_by(nro=vta.nro).first()
        if vta is None:
            return False
        else:
            self.session.query(Venta).filter_by(nro=vta.nro).update({Venta.precio_total:vta.precio_total})
            self.session.commit()
        return True

class DatosLineaVenta(object):

    def __init__(self):
        engine = create_engine('mysql://root:root@localhost:3306/soporte-practico08')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()

    def buscar(self, num):
        lineas_v = self.session.query(LineaVenta).filter_by(nro_vta=num).all()
        return lineas_v

    def alta(self, lv):
        self.session.add(lv)
        self.session.commit()
        return lv

    def modificacion(self, lv):
        lv = self.session.query(LineaVenta).filter_by(id_lineaVenta=lv.id_lineaVenta).first()
        if lv is None:
            return False
        else:
            self.session.query(LineaVenta).filter_by(id_lineaVenta=lv.id_lineaVenta).update({LineaVenta.subtotal:lv.subtotal})
            self.session.commit()
        return True

class DatosCompra(object):

    def __init__(self):
        engine = create_engine('mysql://root:root@localhost:3306/soporte-practico08')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()

    def buscar(self, fecha):
        com = self.session.query(Compra).filter_by(fecha=fecha).all()
        return com

    def todos(self):
        compras = self.session.query(Compra).all()
        return compras


    def modificacion(self, com):
        com = self.session.query(Compra).filter_by(nro=com.nro).first()
        if com is None:
            return False
        else:
            self.session.query(Compra).filter_by(nro=com.nro).update({Compra.precio_total:com.precio_total})
            self.session.commit()
        return True

    def alta(self, com):
        self.session.add(com)
        self.session.commit()
        return com

class DatosLineaCompra(object):

    def __init__(self):
        engine = create_engine('mysql://root:root@localhost:3306/soporte-practico08')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()

    def buscar(self, num):
        lineas_c = self.session.query(LineaCompra).filter_by(nro_com=num).all()
        return lineas_c

    def alta(self, lc):
        self.session.add(lc)
        self.session.commit()
        return lc

    def modificacion(self, lc):
        lc = self.session.query(LineaCompra).filter_by(id_lineaCompra=lc.id_lineaCompra).first()
        if lc is None:
            return False
        else:
            self.session.query(LineaCompra).filter_by(id_lineaCompra=lc.id_lineaCompra).update({LineaCompra.subtotal:lc.subtotal})
            self.session.commit()
        return True

