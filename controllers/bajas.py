# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from bajas.py")

def borrar_cliente():
    # obtengo el primer argumento (ver URL)
    id_cliente = request.args[0]
    # busco y borro el registro
    db(db.clientes.id == id_cliente).delete()
    session.flash = "El cliente %s se borro exitosamente" % id_cliente
    # redirijo al usuario al listado
    redirect(URL(c="reportes", f="ReportesClientes"))
