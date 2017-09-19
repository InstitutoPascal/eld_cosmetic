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
    request.vars.nombre_empresa
    session.nombre_empresas=request.vars.nombre_empresa
    request.vars.remitos
    session.remito =request.vars.remitos
    request.vars.fecha
    session.fecha=request.vars.fecha
    print "",session.nombre_empresa
   
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
    return dict(lista=lista, fecha_dia=fecha_dia,)

def ComprasProveedoresProducto():
    producto=db(db.productos.codigo_producto).select()
    perfume=db(db.productos.id>0).select(db.productos.codigo_producto)
    nombre=db(db.productos.nombre).select()
    eld=db(db.productos.id>0).select(db.productos.nombre)
    cat=db(db.productos.categoria).select()
    categoria=db(db.productos.id>0).select(db.productos.categoria)
    request.vars.codigo
    session.codigo=request.vars.codigo
    request.vars.descripcion
    session.nombre=request.vars.descripcion
    request.vars.marcas
    session.marcas=request.vars.marcas
    request.vars.categoria
    session.categorias=request.vars.categoria
    request.vars.cantidad
    session.cantidad=request.vars.cantidad
    
    print "",session.nombre_empresas, session.remito,session.fecha
    return dict(perfume=perfume, eld=eld, categoria=categoria)
def ComprasProveedoresCodigoBarras():
    if request.vars.codigo:
        print "ingrese el codigo", request.vars.codigo
        # revisar que request.vars.codigo cumpla con las validaciones
        session.codigo_barras = request.vars.codigo
        # buscamos el producto en la base datos
        reg= db(db.productos.codigo_barras==session.codigo_barras).select().first()
        if reg:
            # a fines ilustrativos guardamos en la session los datos del producto
            # esto deberia hacerse en el controlador respectivo, y siempre traerlos de la db reg= db(db.productos.codigo_barras==session.codigo_barras).select().first()
            session.codigo_producto = reg.codigo_producto
            session.nombre= reg.descripcion
            session.marca = reg.marca
            session.categoria= reg.categoria
            session.flash="codigo ok"
            redirect(URL(c="compras", f="ComprasProveedoresProducto"))
        else:
            response.flash= "ingrese un codigo de barra "
    return {}

def ComprasProveedoresListados():
    return dict()
def borrar_item():
    return dict()
def ComprasGuardarProducto():
    return dict()
