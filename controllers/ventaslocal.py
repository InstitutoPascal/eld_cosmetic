# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from ventaslocal.py")

def VentasLocal():
    #importamos la fecha del sistema
    import time
    #obtengo la fecha 
    fecha_dia= time.strftime("%x")
    # obtenemos el usuario logeado en el sistema para enviarlo a la vista
    usuario_log = db(db.auth_user.id == auth.user_id ).select()
    # definir los campos a obtener desde la base de datos:
    campos = db.clientes.id, db.clientes.nombre, db.clientes.codigo_cliente
    # definir la condición que deben cumplir los registros:
    criterio = db.clientes.id>0
    # ejecutar la consulta:
    lista_clientes = db(criterio).select(*campos)
    # revisar si la consulta devolvio registros:
    if not lista_clientes:
        mensaje = "No ha cargado clientes"
    else:
        mensaje = "Seleccione un cliente"
    #redirije los valores al HTML
    return dict(message=mensaje, lista_clientes=lista_clientes, usuario_log=usuario_log, fecha_dia=fecha_dia, )


def VentasLocalTarjeta():
    return dict()

def Borrar_Item():
    # eliminar el elemento de la lista en posicion pos
    del session["items_venta"][int(request.vars.pos)]
    return dict()

def CancelarVenta():
    return dict()

def VentasLocalVistaprevia():
    return dict()

def VentasMediosPago():
    return dict()

def VentasLocalCarga():
    #importamos la fecha del sistema
    import time
    # obtenemos el usuario logeado en el sistema para enviarlo a la vista
    usuario_log = db(db.auth_user.id == auth.user_id ).select()
    # Si se presiono el boton =_enviar en el formulario
    if request.vars["boton_enviar"]:
        print "cliente ",request.vars["id_cliente"]
        # obtengo los valores completados en el formulario
        id_cliente = request.vars["id_cliente"]
        fecha_dia = request.vars.fecha
        usuario_actual  = request.vars.userlog
        # guardo los datos elegidos en la sesión
        session["id_cliente"] = id_cliente
        session["fecha_dia"] = fecha_dia
        session["first_name"] = usuario_actual
         #Defino en la sesion que inicie una lista en blanco
        session["items_venta"] = []
    if request.vars["agregar_item"]:
        # obtengo los valores del formulario
        codigo_barras = request.vars["id_producto"]
        # revisar que request.vars.codigo cumpla con las validaciones
        #session.codigo_barras = request.vars.id_producto
        # buscamos el producto en la base datos
        reg_producto = db(db.productos.codigo_barras==codigo_barras).select().first()
        id_producto = reg_producto.id_producto
        cantidad = request.vars["cantidad"]
        item = {"id_producto": id_producto, "cantidad": int(cantidad)}
        # busco en la base de datos el registro del producto seleccionado
        #reg_producto = db(db.productos.id_producto==id_producto).select().first()
        item["descripcion"] = reg_producto.descripcion
        item["precio"] = reg_producto.precio
        item["alicuota_iva"] = reg_producto.alicuota_iva
        # guardo el item en la sesión
        session["items_venta"].append(item)
    #print"usuario ",session["vendedor_logueado"]
    return dict(id_cliente=session["id_cliente"], fecha_dia=session["fecha_dia"], vendedor_logueado=session["vendedor_logueado"], usuario_log=usuario_log, items_venta=session["items_venta"],)

def confirmar():
    reg_cliente = db(db.clientes.id==session["id_cliente"]).select().first()
    total = 0
    for item in session["items_venta"]:
        total += (item["precio"] * item["cantidad"] + item["precio"] * item["cantidad"] *item["alicuota_iva"]/100.00)
    return dict (mensaje= "Finalizar venta",
                 id_cliente=session["id_cliente"],
                 fecha=session["fecha"],
                 nro_cbte=session["numero_factura"],
                 reg_cliente=reg_cliente, total=total)


def VentaLocalReporte():
    grid = SQLFORM.grid(db.productos)
    return {"grilla": grid}
