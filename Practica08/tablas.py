from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, BIGINT, INTEGER, VARCHAR, FLOAT, DATE, ForeignKey
from sqlalchemy import create_engine

engine = create_engine('mysql://root:root@localhost:3306/soporte-practico08')
Base = declarative_base()
Base.metadata.bind = engine


class Articulo(Base):
    __tablename__ = 'articulos'
    codigo = Column(BIGINT, primary_key=True, unique=True)
    desc = Column(VARCHAR(250))
    precio_com = Column(FLOAT)
    precio_vta = Column(FLOAT)
    stock_real = Column(INTEGER)
    cuit_prov = Column(BIGINT, ForeignKey('proveedores.cuit'))
    lv = relationship('LineaVenta')
    lc = relationship('LineaCompra')

class Proveedor(Base):
    __tablename__ = 'proveedores'
    cuit = Column(BIGINT, primary_key=True, unique=True)
    razon_social = Column(VARCHAR(250))
    telefono = Column(BIGINT)
    estado = Column(VARCHAR(250))
    art = relationship('Articulo')
    compra = relationship('Compra')


class Venta(Base):
    __tablename__ = 'ventas'
    nro = Column(BIGINT, autoincrement=True, primary_key=True, unique=True)
    fecha = Column(DATE)
    precio_total = Column(FLOAT)
    lv = relationship('LineaVenta')


class LineaVenta(Base):
    __tablename__ = 'lineas_venta'
    id_lineaVenta = Column(BIGINT, autoincrement=True, primary_key=True, unique=True)
    nro_vta = Column(BIGINT, ForeignKey('ventas.nro'))
    cod_art = Column(BIGINT, ForeignKey('articulos.codigo'))
    cantidad = Column(INTEGER)
    subtotal = Column(FLOAT)

class Compra(Base):
    __tablename__ = 'compras'
    nro = Column(BIGINT, autoincrement=True, primary_key=True, unique=True)
    fecha = Column(DATE)
    precio_total = Column(FLOAT)
    proveedor = Column(BIGINT, ForeignKey('proveedores.cuit'))
    lc = relationship('LineaCompra')


class LineaCompra(Base):
    __tablename__ = 'lineas_compra'
    id_lineaCompra = Column(BIGINT, autoincrement=True, primary_key=True, unique=True)
    nro_com = Column(BIGINT, ForeignKey('compras.nro'))
    cod_art = Column(BIGINT, ForeignKey('articulos.codigo'))
    cantidad = Column(INTEGER)
    subtotal = Column(FLOAT)

def crear_tabla():
    Base.metadata.create_all(engine)

crear_tabla()
