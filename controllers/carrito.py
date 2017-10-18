# -*- coding: utf-8 -*-
# intente algo como
def index(): 
    if request.vars["producto"]:
        # obtengo los valores del formulario
        id_prod = request.vars["id_producto"]
        print id_prod
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
    return dict(items_venta=session["items_venta"])
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
