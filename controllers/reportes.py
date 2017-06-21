# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from reportes.py")


# ReportesClientes-------------------------------------------------------------------------------------------------------------

def ReportesClientes():
    subtitulo=T('Listado de Clientes')
    listado =db(db.clientes).select(db.clientes.ALL)
    return dict(dc=listado)
#-------------------------------------------------------------------------------------------------------------------------------------
# ReportesProveedores

def ReportesProveedores():
    subtitulo=T('Listado de Proveedores')
    listado =db(db.proveedor).select(db.proveedor.ALL)
    return dict(dc=listado)
#------------------------------------------------------------------------------------------------------------------------------------------------------
#reportes por productos
def ReportesProductos():
    subtitulo=T('Listado de Productos')
    listado =db(db.productos).select(db.productos.ALL)
    return dict(dc=listado)

#------------------------------------------------------------------------------------------------------------------------------------------------------------#Reportes de empleados

def ReportesEmpleados():
    subtitulo=T('Listado de Empleados')
    listado =db(db.empleados).select(db.empleados .ALL)
    return dict(dc=listado)

#------------------------------------------------------------------------------------------------------------------------------------------------------------#Reportes de VentasLocal
def ReportesVentasLocal():

    return dict()

#------------------------------------------------------------------------------------------------------------------------------------------------------------#Reportes de VentasOnline
def ReportesVentasOnline():

    return dict()
#------------------------------------------------------------------------------------------------------------------------------------------------------------#Reportes de Remitos
def ReportesRemitos():

    return dict()
#------------------------------------------------------------------------------------------------------------------------------------------------------------#Reportes de Remitos
def RemitosDetalles():

    return dict()
