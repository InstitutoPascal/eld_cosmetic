# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from ventaslocal.py")

def VentasLocal():
    #importamos la fecha del sistema
    import time
    #obtengo la fecha 
    fecha_dia= time.strftime("%x")
    # obtenemos el usuario logeado en el sistema para enviarlo a la vista
    usuario = db(db.auth_user.id == auth.user_id ).select()
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
    return dict(message=mensaje, lista_clientes=lista_clientes, usuario=usuario, fecha_dia=fecha_dia,)


def VentasLocalTarjeta():
    return dict()

def Borrar_Item():
    return dict()

def CancelarVenta():
    return dict()

def VentasLocalVistaprevia():
    return dict()

def VentasMediosPago():
    return dict()

def VentasLocalCarga():
    return dict()


def VentaLocalReporte():
    grid = SQLFORM.grid(db.productos)
    return {"grilla": grid}
