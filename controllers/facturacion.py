# -*- coding: utf-8 -*-
# intente algo como

import datetime
from ConfigParser import SafeConfigParser

def obtener_cae():
    from pyafipws.wsaa import WSAA
    from pyafipws.wsfev1 import WSFEv1

    # web service de factura electronica:
    wsfev1 = WSFEv1()
    wsfev1.LanzarExcepciones = True

    # obteniendo el TA para pruebas
    ta = WSAA().Autenticar("wsfe", "/home/sysadmin/web2py/cert/empresa.crt",
                                   "/home/sysadmin/web2py/cert/empresa.key", debug=True)
    wsfev1.SetTicketAcceso(ta)
    wsfev1.Cuit = "20261463041"

    ok = wsfev1.Conectar()

    # obtengo el id de comprobante pasado por la URL desde la funcion facturar
    factura_id = int(request.args[0])
    # obtengo el registro general del comprobante (encabezado y totales)
    reg = db(db.comprobante_afip.id==factura_id).select().first()

    tipo_cbte = reg.tipo_cbte
    punto_vta = reg.punto_vta
    cbte_nro = long(wsfev1.CompUltimoAutorizado(tipo_cbte, punto_vta) or 0) + 1
    #fecha = reg.fecha_cbte.strftime("%Y%m%d")  # formato AAAAMMDD
    fecha = datetime.datetime.now().strftime("%Y%m%d")
    concepto = reg.concepto
    tipo_doc = reg.tipo_doc # 80: CUIT, 96: DNI
    nro_doc = reg.nro_doc.replace("-", "") # del cliente, sin rayita
    cbt_desde = cbte_nro; cbt_hasta = cbte_nro
    imp_total = reg.imp_total
    imp_tot_conc = reg.imp_tot_conc
    imp_neto = reg.imp_neto
    imp_iva = reg.impto_liq
    imp_trib = "0.00"
    imp_op_ex = reg.imp_op_ex
    fecha_cbte = fecha
    # Fechas del per�odo del servicio facturado y vencimiento de pago:
    if concepto > 1:
        fecha_venc_pago = reg.fecha_venc_pago
        fecha_serv_desde = reg.fecha_serv_desde
        fecha_serv_hasta = reg.fecha_serv_desde
    else:
        fecha_venc_pago = fecha_serv_desde = fecha_serv_hasta = None
    moneda_id = "PES"
    moneda_ctz = "1.000"

    wsfev1.CrearFactura(concepto, tipo_doc, nro_doc, 
                tipo_cbte, punto_vta, cbt_desde, cbt_hasta , 
                imp_total, imp_tot_conc, imp_neto,
                imp_iva, imp_trib, imp_op_ex, fecha_cbte, fecha_venc_pago, 
                fecha_serv_desde, fecha_serv_hasta, #--
                moneda_id, moneda_ctz)

    # subtotales por alicuota de IVA:
    iva_id = 5 # 21%
    base_imp = reg.imp_neto   # neto al 21%
    importe = reg.impto_liq     # iva liquidado al 21%
    wsfev1.AgregarIva(iva_id, base_imp, importe)

    try:
        wsfev1.CAESolicitar()
    except:
        print "uy le mandamos fruta!"

    #print "Nro. Cbte. desde-hasta", wsfev1.CbtDesde, wsfev1.CbtHasta
    #print "Resultado", wsfev1.Resultado
    #print "Reproceso", wsfev1.Reproceso
    #print "CAE", wsfev1.CAE
    #print "Vencimiento", wsfev1.Vencimiento
    #print "Observaciones", wsfev1.Obs

    # actualizamos la factura con la respuesta de AFIP
    db(db.comprobante_afip.id == factura_id).update(
        cae=wsfev1.CAE,
        fecha_cbte=fecha,
        cbte_nro=cbte_nro,
        fecha_vto=wsfev1.Vencimiento,
        )

    if wsfev1.CAE:
        redirect(URL(f="generar_pdf", args=[factura_id]))
    response.view = "generic.html"
    return {"Nro. Cbte. desde-hasta": wsfev1.CbtDesde,
            "Resultado": wsfev1.Resultado,
            "Reproceso": wsfev1.Reproceso,
            "CAE": wsfev1.CAE,
            "Vencimiento": wsfev1.Vencimiento,
            "Observaciones": wsfev1.Obs,
            "XmlRequest": wsfev1.XmlRequest,
            "XmlResponse": wsfev1.XmlResponse,
            "ErrMsg": wsfev1.ErrMsg,
          }

def generar_pdf(): 
    CONFIG_FILE = "/home/sysadmin/pyafipws/rece.ini"

    config = SafeConfigParser()
    config.read(CONFIG_FILE)
    conf_fact = dict(config.items('FACTURA'))
    conf_pdf = dict(config.items('PDF'))

    from pyafipws.pyfepdf import FEPDF
    fepdf = FEPDF()

    # cargo el formato CSV por defecto (factura.csv)
    fepdf.CargarFormato(conf_fact.get("formato", "factura.csv"))

    # establezco formatos (cantidad de decimales) según configuración:
    fepdf.FmtCantidad = conf_fact.get("fmt_cantidad", "0.2")
    fepdf.FmtPrecio = conf_fact.get("fmt_precio", "0.2")


    # creo una factura de ejemplo
    HOMO = True


    # obtengo el registro general del comprobante (encabezado y totales)
    id_comprobante = int(request.args[0])
    reg = db(db.comprobante_afip.id==id_comprobante).select().first()

    tipo_cbte = reg.tipo_cbte
    punto_vta = reg.punto_vta
    cbte_nro = reg.cbte_nro
    fecha = reg.fecha_cbte #.strftime("%Y%m%d")  # formato AAAAMMDD
    concepto = reg.concepto
    tipo_doc = reg.tipo_doc # 80: CUIT, 96: DNI
    nro_doc = reg.nro_doc.replace("-", "") # del cliente, sin rayita
    cbt_desde = cbte_nro; cbt_hasta = cbte_nro
    imp_total = reg.imp_total
    imp_tot_conc = reg.imp_tot_conc
    imp_neto = reg.imp_neto
    imp_iva = reg.impto_liq
    imp_trib = "0.00"
    imp_op_ex = reg.imp_op_ex
    fecha_cbte = fecha
    # Fechas del per�odo del servicio facturado y vencimiento de pago:
    if concepto > 1:
        fecha_venc_pago = reg.fecha_venc_pago
        fecha_serv_desde = reg.fecha_serv_desde
        fecha_serv_hasta = reg.fecha_serv_desde
    else:
        fecha_venc_pago = fecha_serv_desde = fecha_serv_hasta = None
    moneda_id = reg.moneda_id
    moneda_ctz = reg.moneda_ctz

    # datos generales del encabezado:
    incoterms = 'FOB'                   # solo exportación
    idioma_cbte = 1                     # 1: es, 2: en, 3: pt

    # datos adicionales del encabezado:
    nombre_cliente = reg.nombre_cliente
    domicilio_cliente = reg.domicilio_cliente
    pais_dst_cmp = 212                  # 200: Argentina, ver tabla
    id_impositivo = reg.id_impositivo      # cat. iva (mercado interno)
    forma_pago = reg.forma_pago

    obs_generales = reg.obs
    obs_comerciales = reg.obs_comerciales

    # datos devueltos por el webservice (WSFEv1, WSMTXCA, etc.):
    motivo_obs = "Factura individual, DocTipo: 80, DocNro 30000000007 no se encuentra registrado en los padrones de AFIP."
    cae = reg.cae
    fch_venc_cae = reg.fecha_vto

    fepdf.CrearFactura(concepto, tipo_doc, nro_doc, tipo_cbte, punto_vta,
        cbte_nro, imp_total, imp_tot_conc, imp_neto,
        imp_iva, imp_trib, imp_op_ex, fecha_cbte, fecha_venc_pago, 
        fecha_serv_desde, fecha_serv_hasta, 
        moneda_id, moneda_ctz, cae, fch_venc_cae, id_impositivo,
        nombre_cliente, domicilio_cliente, pais_dst_cmp, 
        obs_comerciales, obs_generales, forma_pago, incoterms, 
        idioma_cbte, motivo_obs)

    # completo campos extra del encabezado:
    ok = fepdf.EstablecerParametro("localidad_cliente", "Hurlingham")
    ok = fepdf.EstablecerParametro("provincia_cliente", "Buenos Aires")

    # imprimir leyenda "Comprobante Autorizado" (constatar con WSCDC!)
    ok = fepdf.EstablecerParametro("resultado", "A")

    # tributos adicionales:
    tributo_id = 99
    desc = 'Impuesto Municipal Matanza'
    base_imp = "100.00"
    alic = "1.00"
    importe = "1.00"
    fepdf.AgregarTributo(tributo_id, desc, base_imp, alic, importe)

    tributo_id = 4
    desc = 'Impuestos Internos'
    base_imp = None
    alic = None
    importe = "0.00"
    fepdf.AgregarTributo(tributo_id, desc, base_imp, alic, importe)

    # subtotales por alícuota de IVA:
    iva_id = 5 # 21%
    base_imp = 100
    importe = 21
    fepdf.AgregarIva(iva_id, base_imp, importe)

    # detalle de artículos:
    registros = db(db.detalle_afip.comprobante_id==id_comprobante).select()
    for registro in registros:
        u_mtx = 123456
        cod_mtx = 1234567890123
        codigo = registro.codigo
        ds = registro.ds
        qty = registro.qty
        umed = 7
        precio = registro.precio
        imp_iva = registro.imp_iva
        bonif = 0.00
        iva_id = registro.iva_id
        importe = registro.imp_total
        despacho = u''
        dato_a = ""
        fepdf.AgregarDetalleItem(u_mtx, cod_mtx, codigo, ds, qty, umed, 
                precio, bonif, iva_id, imp_iva, importe, despacho, dato_a)

    # descuento general (a tasa 21%):
    u_mtx = cod_mtx = codigo = None
    ds = u"Bonificación/Descuento 10%"
    qty = precio = bonif = None
    umed = 99
    iva_id = 5
    if tipo_cbte in (1, 2, 3, 4, 5, 34, 39, 51, 52, 53, 54, 60, 64):
        # discriminar IVA si es clase A / M
        imp_iva = -2.21
    else:
        imp_iva = None
    importe = -12.10
    fepdf.AgregarDetalleItem(u_mtx, cod_mtx, codigo, ds, qty, umed, 
            precio, bonif, iva_id, imp_iva, importe, "")

    # descripción (sin importes ni cantidad):
    u_mtx = cod_mtx = codigo = None
    qty = precio = bonif = iva_id = imp_iva = importe = None
    umed = 0
    ds = u"Descripción Ejemplo"
    fepdf.AgregarDetalleItem(u_mtx, cod_mtx, codigo, ds, qty, umed, 
            precio, bonif, iva_id, imp_iva, importe, "")

    # completo campos personalizados de la plantilla:
    fepdf.AgregarDato("custom-nro-cli", "Cod.123")
    fepdf.AgregarDato("custom-pedido", "1234")
    fepdf.AgregarDato("custom-remito", "12345")
    fepdf.AgregarDato("custom-transporte", "Camiones Ej.")

    # datos fijos:
    for k, v in conf_pdf.items():
        fepdf.AgregarDato(k, v)
        if k.upper() == 'CUIT':
            fepdf.CUIT = v  # CUIT del emisor para código de barras

    fepdf.CrearPlantilla(papel=conf_fact.get("papel", "legal"), 
                         orientacion=conf_fact.get("orientacion", "portrait"))
    fepdf.ProcesarPlantilla(num_copias=int(conf_fact.get("copias", 1)),
                            lineas_max=int(conf_fact.get("lineas_max", 24)),
                            qty_pos=conf_fact.get("cant_pos") or 'izq')

    salida = "/tmp/factura.pdf"
    fepdf.GenerarPDF(archivo=salida)
    ##fepdf.MostrarPDF(archivo=salida,imprimir=False)

    response.headers['Content-Type'] = "application/pdf"
    return open(salida, "rb")
