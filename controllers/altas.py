# -*- coding: utf-8 -*-
# intente algo como
#def index(): return dict(message="hello from altas.py")



#alta_cliente
def alta_cliente():
    form = SQLFORM(db.clientes)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

def alta_transporte():
    form = SQLFORM(db.transporte)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)
    

#alta_proveedor
def alta_proveedor():
    form = SQLFORM(db.proveedor)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

#alta_producto
def alta_producto():
    form = SQLFORM(db.productos)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)



#alta_empleado
def alta_empleado():
    form = SQLFORM(db.empleados)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

#alta_stock
def alta_stock():
    form = SQLFORM(db.stock)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

#---------------------------------------------------------------------------------------------------------------------------------------06-04-2017-------
# alta_venta
def alta_venta():
    form = SQLFORM(db.ventas)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)
