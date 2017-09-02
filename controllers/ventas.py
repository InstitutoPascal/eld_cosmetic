# -*- coding: utf-8 -*-
# try something like
def VentasLocal():
    return dict()

def VentasLocalTarjeta():
    return dict()

def Borrar_Item():
    return dict()

def CancelarVenta():
    return dict()

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

def VentasLocalCarga():
    return dict()

def VentasLocalVistaprevia():
    return dict()

def VentasMediosPago():
    return dict()

def inicio():
    "pagina de inicio del catalogo"
    return dict(message="funcion  inicio")

def VentasOnlinecatalogo():
    return dict()

def VentasOnlineCarga():
    return dict()

def VentasOnlinePerfume1():
    return dict()

def VentasOnlinePerfume2():
    return dict()

def VentasOnlinePerfume3():
    return dict()

def VentasOnlinePerfume4():
    return dict()

def VentasOnlinePerfume5():
    return dict()

def VentasOnlinePerfume6():
    return dict()

def VentasOnlinePerfume7():
    return dict()

def VentasOnlinePerfume8():
    return dict()

def VentasOnlinePerfume9():
    return dict()

def VentasOnlinePerfume10():
    return dict()

def VentasOnlinePerfume11():
    return dict()

def VentasOnlinePerfume12():
    return dict()

def VentasOnlinePerfume13():
    return dict()

def VentasOnlinePerfume14():
    return dict()

def VentasOnlinePerfume15():
    return dict()

def VentasOnlinePerfume16():
    return dict()

def VentasOnlinePerfume17():
    return dict()

def VentasOnlinePerfume18():
    return dict()

def VentasOnlineHome():
    return dict()

def VentaLocalReporte():
    grid = SQLFORM.grid(db.productos)
    return {"grilla": grid}

def ventasonlinevistaprevia():
    return dict()
