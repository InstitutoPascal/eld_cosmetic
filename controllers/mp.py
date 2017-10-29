# -*- coding: utf-8 -*-
import mercadopago
import json
import os, sys
def index():
    mp = mercadopago.MP(myconf.take('mercadopago.client_id'), myconf.take('mercadopago.client_secret'))
    print(myconf.take('mercadopago.client_id'), myconf.take('mercadopago.client_secret'))
    # creamos un dict con los datos del pago solicitado:
    preference = {
		"items": [
			{
				"title": item["descripcion"],
				"unit_price": item["precio"],
                "quantity": item["cantidad"],
                "currency_id": "ARS",
				"picture_url": "https://www.mercadopago.com/org-img/MP3/home/logomp3.gif"
			}
		for item in session["items_venta"]],
        "marketplace_fee": 2.29 # fee to collect
	}
    # llamamos a MP para que cree un link...
    preferenceResult = mp.create_preference(preference)
    try:
        url = preferenceResult["response"]["sandbox_init_point"]
        redirect(url)
    except:
        raise
        response.view = "generic.html"
        return {"pref": preferenceResult}
