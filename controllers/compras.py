# -*- coding: utf-8 -*-

#compras
def ComprasProveedores():
    #importamos la fecha del sistema
    import time
    #obtengo la fecha 
    fecha_dia= time.strftime("%x")
    # los datos de la variable fecha_dia lo guardamos en la session.fecha temporalmente
    session.fecha = fecha_dia
    # obtenemos el usuario logeado en el sistema para enviarlo a la vista
    usuario_log = db(db.auth_user.id == auth.user_id ).select()
    # definir los campos a obtener desde la base de datos:
    campos = db.proveedor.id, db.proveedor.nombre_empresa
    # definir la condición que deben cumplir los registros:
    criterio = db.proveedor.id>0
    # ejecutar la consulta:
    lista_proveedor = db(criterio).select(*campos)
    # revisar si la consulta devolvio registros:
    
    if not lista_proveedor:
        mensaje = "No ha cargado proveedor"
    else:
        mensaje = "Seleccione un proveedor"
    #redirije los valores al HTML
    return dict(message=mensaje, lista_proveedor=lista_proveedor, usuario_log=usuario_log, fecha_dia=fecha_dia, )




def ComprasProveedoresListados():
   
    #importamos la fecha del sistema
    import time
    #obtenemos el usuario logeado en el sistema para enviarlo a la vista por medio del return
    usuario_log = db(db.auth_user.id == auth.user_id ).select()
   
    # obtengo los valores completados en el formulario
    id_proveedor = request.vars["proveedor_id"]
    reg_proveedor = db(db.proveedor.id==id_proveedor).select().first()
    
    #Si se presiono el boton =_enviar en el formulario
    if request.vars["boton_enviar"]:
        fecha_dia = request.vars.fecha
        session.fecha= fecha_dia
        remito=request.vars.remito
        session["remito"] = remito
        
        usuario_actual  = request.vars.userlog
        # guardo los datos elegidos en la sesión
        session["id_proveedor"] = id_proveedor
        session["fecha_dia"] = fecha_dia
        session["first_name"] = usuario_actual
         #Defino en la sesion que inicie una lista en blanco
        session["items_venta"] = []
        reg_proveedor = db(db.proveedor.id==id_proveedor).select().first()

        
       
    if request.vars["agregar_item"]:
        # obtengo los valores del formulario
        codigo_barras = request.vars["id_producto"]
        # buscamos el producto en la base datos
        reg_producto = db(db.productos.codigo_barras==codigo_barras).select().first()
        id_producto = reg_producto.id_producto
        cantidad = request.vars["cantidad"]
        item = {"id_producto": id_producto, "cantidad": int(cantidad),}
        item["descripcion"] = reg_producto.descripcion
        item["codigo"]= reg_producto.codigo_producto
        item["nombre"]=reg_producto.nombre
        item["marca"]=reg_producto.marca
        item["precio"] = reg_producto.precio
        # guardo el item en la sesión
        session["items_venta"].append(item)


    return dict(fecha_dia=session["fecha_dia"], vendedor_logueado=session["vendedor_logueado"],usuario_log=usuario_log, items_venta=session["items_venta"], id_proveedor=id_proveedor,)

    


def borrar_item(): # eliminar el elemento de la lista en posicion pos
    del session["items_venta"][int(request.vars.pos)]
    return dict()

def confirmar_compra():
    return dict()

def ComprasGuardarProducto():
    # se guardan los datos obtenidos de la session.fecha  a una variable fecha
    fecha= session.fecha
    rem = session.remito
    
    session["items_venta"]
    # realizamos un for en session item_venta
    for item in session["items_venta"]:
        descripcion = item["descripcion"]
        cantidad = item["cantidad"]
        precio_un = item["precio"]
        nombre = item ["nombre"]
        marca = item ["marca"]
        codigo= item ["codigo"]
        
        
        db.compras.insert(
                categoria=descripcion,
                cantidad=cantidad,
                precio=precio_un,
                nombre=nombre,
                codigo_producto=codigo,
                marca= marca,
                remito=rem,
                fecha_ingreso= fecha
                
            )


    print "lista productos", session["items_venta"]
    return dict()

def cancelar_venta():
    del session["items_venta"]
    return dict()
