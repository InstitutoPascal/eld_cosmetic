# -*- coding: utf-8 -*-
#compras
def ComprasProveedores():
    #importamos la fecha del sistema
    import time
    #obtengo la fecha 
    fecha_dia= time.strftime("%x")
   
    #provee = db(db.proveedor.Nombre_Empresa == Nombre_Empresa ).select()
    # definir los campos a obtener desde la base de datos:
    proveedor=db(db.proveedor.nombre_empresa).select()
    lista=db(db.proveedor.id>0).select(db.proveedor.nombre_empresa)
    
    # definir la condición que deben cumplir los registros:
    #criterio = db.proveedor.nombre_empresa>0
    # ejecutar la consulta:
    #ista_clientes = db(criterio).select(*campos)
    # revisar si la consulta devolvio registros:
    #if not lista_clientes:
        #ensaje = "No ha cargado un proveedor"
    #else:
     #   mensaje = "Seleccione un proveedor"
    #redirije los valores al HTML
    return dict(lista=lista, fecha_dia=fecha_dia )

def ComprasProveedoresProducto():
    producto=db(db.productos.codigo_producto).select()
    perfume=db(db.productos.id>0).select(db.productos.codigo_producto)
    nombre=db(db.productos.nombre).select()
    eld=db(db.productos.id>0).select(db.productos.nombre)
    cat=db(db.productos.categoria).select()
    categoria=db(db.productos.id>0).select(db.productos.categoria)
    
    
    return dict(perfume=perfume, eld=eld, categoria=categoria)
def ComprasProveedoresListados():
    return dict()
def borrar_item():
    return dict()
def ComprasGuardarProducto():
    return dict()
