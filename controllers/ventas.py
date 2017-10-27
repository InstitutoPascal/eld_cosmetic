import datetime
from ConfigParser import SafeConfigParser

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

def GenerarFactura():
    # creamos un registro de factura (encabezado) 
    # UDS DEBEN TRAER LOS DATOS DE SU SISTEMA (tablas cliente, productos, etc.)
    moneda = db(db.moneda.codigo=="DOL").select().first()
    # busco el registro del cliente en la base (usando el id de la sesion)
    id_cliente = session["id_cliente"]
    reg_cliente = db(db.clientes.id==id_cliente).select().first()
    factura_id = db.comprobante_afip.insert(
            webservice="wsfev1",
            #fecha_cbte=datetime.datetime.now(),
            tipo_cbte=1,  # factura A, ver tabla tipos_cbte
            punto_vta=PUNTO_VTA,
            cbte_nro=1,
            # Datos del cliente (traer de la tabla respectiva!!!!!!)
            nombre_cliente=reg_cliente.nombre + " " + reg_cliente.apellido,
            tipo_doc=80,#96 dni # 80 cuit
            nro_doc=reg_cliente.cuil,
            domicilio_cliente=reg_cliente.direccion,
            telefono_cliente=reg_cliente.telefono,
            localidad_cliente=reg_cliente.localidad_cliente,
            provincia_cliente=reg_cliente.provincia,
            email=reg_cliente.email,
            id_impositivo=reg_cliente.tipo_categoria,
            moneda_id=moneda.id,
            )

    total_neto = 0
    total_iva = 0
    # recorro los productos en el carrito (session)
    for item in session["items_venta"]:
        descripcion = item["descripcion"]
        cantidad = item["cantidad"]
        precio_un = item["precio"]
        neto =  (precio_un * cantidad)
        importe_iva = neto * 0.21
        subtotal = neto + importe_iva
        total_neto = total_neto + neto
        total_iva = total_iva + importe_iva
        db.detalle_afip.insert(
                comprobante_id=factura_id,
                codigo="P001",
                ds=descripcion,
                precio=precio_un,
                qty=cantidad,
                umed=7,
                iva_id=5,  # 21%
                imp_iva=importe_iva,
                imp_total=subtotal
            )

    # actualizar totales factura:
    db(db.comprobante_afip.id == factura_id).update(
             imp_total = total_neto + total_iva,
             imp_tot_conc = 0,
             imp_neto = total_neto,
             impto_liq = total_iva,
             ##imp_trib = "0.00"
             imp_op_ex = 0,
        )

    ## db.alicutoa_iva.insert()

    redirect(URL(c="facturacion", f="obtener_cae", args=[factura_id]))
    return dict(message="se creo la factura %s" % factura_id)
