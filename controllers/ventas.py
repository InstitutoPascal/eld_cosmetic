# -*- coding: utf-8 -*-
# try something like
# -*- coding: utf-8 -*-

def VentasOnlinetarjeta():
    # creamos un dict con los datos del pago solicitado:
    preference = {
		"items": [
			{
				"title": "Perfume El Polakkko",
				"description": "Botellita 50ml de escencia saraza saraza ...",
				"quantity": 1,
				"unit_price": 50,
				"currency_id": "ARS",
				"picture_url": "https://www.mercadopago.com/org-img/MP3/home/logomp3.gif"
			}
		],
		"marketplace_fee": 2.29 # fee to collect
	}
    # llamamos a MP para que cree un link...
    preferenceResult = mp.create_preference(preference)
    url = preferenceResult["response"]["sandbox_init_point"]
    return dict(url_boton=url)


def inicio():
    "pagina de inicio del catalogo"
    return dict(message="funcion  inicio")

def VentasOnlinecatalogo():
    return dict()

def VentasOnlineCarga():
    #importamos la fecha del sistema
    import time
     # obtenemos el usuario logeado en el sistema para enviarlo a la vista
    usuario_log = db(db.auth_user.id == auth.user_id ).select()
    if request.vars["boton_enviar"]:
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
        id_producto = request.vars["id_producto"]
        cantidad = request.vars["cantidad"]
        item = {"id_producto": id_producto, "cantidad": int(cantidad)}
        # busco en la base de datos el registro del producto seleccionado
        reg_producto = db(db.productos.id_producto==id_producto).select().first()
        item["descripcion"] = reg_producto.descripcion
        item["precio"] = reg_producto.precio
        item["alicuota_iva"] = reg_producto.alicuota_iva
        # guardo el item en la sesión
        session["items_venta"].append(item)
    #obtengo la lista de productos
    lista_productos = db(db.productos.id>0).select()
    print"usuario ",session["vendedor_logueado"]
    return dict(id_cliente=session["id_cliente"], fecha_dia=session["fecha_dia"], vendedor_logueado=session["vendedor_logueado"],lista_productos=lista_productos, usuario_log=usuario_log, items_venta=session["items_venta"],)


def VentasOnlineHome():
    return dict()

def VentaLocalReporte():
    grid = SQLFORM.grid(db.productos)
    return {"grilla": grid}

def ventasonlinevistaprevia():
    return dict()

def carrito():
    return dict()
