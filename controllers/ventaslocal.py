# -*- coding: utf-8 -*-
# intente algo como

import datetime
from ConfigParser import SafeConfigParser
#response.view = "generic.html"

@auth.requires_login()
def VentasLocal():
    #importamos la fecha del sistema
    import time
    #obtengo la fecha 
    fecha_dia= time.strftime("%x")
    # obtenemos el usuario logeado en el sistema para enviarlo a la vista
    #usuario_log = db(db.auth_user.id == auth.user_id ).select()
    usuario_log = db(db.empleados.usuario_id == auth.user_id ).select().first()
    vendedor_log = usuario_log.nombre
    print "usuario logueado ", vendedor_log
    session["vendedor_log"] = vendedor_log
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
    return dict(message=mensaje, lista_clientes=lista_clientes, vendedor_log=vendedor_log, fecha_dia=fecha_dia, )

def Borrar_Item():
    # eliminar el elemento de la lista en posicion pos
    del session["items_venta"][int(request.vars.pos)]
    return dict()

def CancelarVenta():
    # elimina todos los elementos de la lista
    del session["items_venta"]
    return dict()

def VentasMediosPago():
    total = 0
    #Recorro lo almacenado en items_venta en la session y hago los calculos de los impuesto para enviarlos a la confirmacion
    for item in session["items_venta"]:
        total += (item["precio"] * item["cantidad"] + item["precio"] * item["cantidad"] *item["alicuota_iva"]/100.00)
    return dict (id_cliente=session["id_cliente"], fecha_dia=session["fecha_dia"], total=total)

def VentasLocalCarga():
    #importamos la fecha del sistema
    import time
    if "id_cliente" in request.vars:
        session["id_cliente"] = request.vars["id_cliente"]  # traer del form y guardo en la sesion
    cliente = db(db.clientes.id == session["id_cliente"] ).select().first()
    cliente_venta = cliente.nombre
    print "el cliente es: ",cliente_venta
    # obtenemos el usuario logeado en el sistema para enviarlo a la vista
    #####usuario_log = db(db.auth_user.id == auth.user_id ).select()
    # Si se presiono el boton =_enviar en el formulario
    if request.vars["boton_enviar"]:

        # obtengo los valores completados en el formulario
        id_cliente = request.vars["id_cliente"]
        fecha_dia = request.vars.fecha
        usuario_actual  = request.vars.userlog
        # guardo los datos elegidos en la sesión
        session["id_cliente"] = id_cliente
        session["fecha_dia"] = fecha_dia
        #session["first_name"] = usuario_actual
        #Defino en la sesion que inicie una lista en blanco
        session["items_venta"] = []
    if request.vars["agregar_item"]:
        # obtengo los valores del formulario
        codigo_barras = request.vars["id_producto"]
        # busco en la base de datos el codigo de barras ingresado, lo comparo y obtengo los campos de la tabla productos
        reg_producto = db(db.productos.codigo_barras==codigo_barras).select().first()
        # obtengo el id de la consulta anterior
        id_producto = reg_producto.id_producto
        # obtengo la candidad de productos ingresado en el formulario
        cantidad = request.vars["cantidad"]
        # creo un diccionario y lo inicializo con el id y la cantidad de producto
        item = {"id_producto": id_producto, "cantidad": int(cantidad)}
        # agrego nuevos registros en el diccionario (item["nombredelaclave"] = variablequetraelaconsulta.campodelatablaconsultada)
        item["nombre"] = reg_producto.nombre
        item["marca"] = reg_producto.marca
        item["descripcion"] = reg_producto.descripcion
        item["precio"] = reg_producto.precio
        item["alicuota_iva"] = reg_producto.alicuota_iva
        # guardo el item en la sesión
        session["items_venta"].append(item)
    return dict( fecha_dia=session["fecha_dia"], items_venta=session["items_venta"], cliente_venta=cliente_venta, vend=session["vendedor_log"],)

def confirmar():
    total = 0
    #Recorro lo almacenado en items_venta en la session y hago los calculos de los impuesto para enviarlos a la vista de confirmacion
    for item in session["items_venta"]:
        total += (item["precio"] * item["cantidad"] + item["precio"] * item["cantidad"] *item["alicuota_iva"]/100.00)
    return dict (id_cliente=session["id_cliente"], fecha_dia=session["fecha_dia"], total=total)

def VentaLocalReporte():
    grid = SQLFORM.grid(db.productos)
    return {"grilla": grid}


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
