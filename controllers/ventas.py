# -*- coding: utf-8 -*-
# try something like
# -*- coding: utf-8 -*-
import mercadopago
import json
# credenciales del sandbox (sitio de prueba)
CLIENT_ID = "4054022218072284"
CLIENT_SECRET = "SUWu1Tr1pYTRCZQiliTykMJMYxeYYZAm"
# instancio el objeto para comunicarme con MP
mp = mercadopago.MP(CLIENT_ID, CLIENT_SECRET)
# esto es un ejemplo, revisar !!!!!! no subir al repo!!!!
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

def VentasOnlineHome():
    return dict()

def VentaLocalReporte():
    grid = SQLFORM.grid(db.productos)
    return {"grilla": grid}

def ventasonlinevistaprevia():
    return dict()
