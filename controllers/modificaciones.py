# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from modificaciones.py")

def editar_cliente():
    # obtengo el primer argumento (ver URL)
    id_cliente = request.args[0]
    # busco el registro en la bbdd
    cliente =  db(db.clientes.id == id_cliente).select().first()
    # armo el formulario para modificar este registro:
    form=SQLFORM(db.clientes, cliente)
    if form.accepts(request.vars, session):
        session.flash = 'Formulario correctamente cargado'
        # redirijo al usuario al listado
        redirect(URL(c="reportes", f="ReportesClientes"))
    elif form.errors:
		response.flash = 'Su formulario contiene errores, porfavor modifiquelo'
    else:
		response.flash = 'Por favor rellene el formulario'
    return dict(f=form)


# Editar Cliente --------------------------------------------------------------------------------------------
def editar_proveedor():
    # obtengo el primer argumento (ver URL)
    id_proveedor = request.args[0]
    # busco el registro en la bbdd
    proveedor =  db(db.proveedor.id == id_proveedor).select().first()
    # armo el formulario para modificar este registro:
    form=SQLFORM(db.proveedor, proveedor)
    if form.accepts(request.vars, session):
        session.flash = 'Formulario correctamente cargado'
        # redirijo al usuario al listado
        redirect(URL(c="reportes", f="ReportesClientes"))
    elif form.errors:
		response.flash = 'Su formulario contiene errores, porfavor modifiquelo'
    else:
		response.flash = 'Por favor rellene el formulario'
    return dict(f=form)
