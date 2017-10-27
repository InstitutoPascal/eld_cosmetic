# -*- coding: utf-8 -*-
import mercadopago
import json
mp = mercadopago.MP(myconf.take('mercadopago.client_id'), myconf.take('mercadopago.client_secret'))

def index():
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
    output = """
    <!doctype html>
    <html>
        <head>
            <title>Ejemplo MP</title>
        </head>
        <body>
            <a href="{url}">Pagar</a>
        </body>
    </html>
    """.format (url=url)
    return output
