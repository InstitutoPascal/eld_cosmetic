# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(B('web', SPAN(2), 'py'), XML('&trade;&nbsp;'),
                  _class="navbar-brand", _href="http://www.web2py.com/",
                  _id="web2py-logo")
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''

# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu += [
    (T('ELD_Cosmetics'), False, URL('default', 'index'), [])
]

DEVELOPMENT_MENU = True


# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. remove in production
# ----------------------------------------------------------------------------------------------------------------------

def _():
    # ------------------------------------------------------------------------------------------------------------------
    # shortcuts
    # ------------------------------------------------------------------------------------------------------------------
    app = request.application
    ctr = request.controller
    # ------------------------------------------------------------------------------------------------------------------
    # useful links to internal and external resources
    # ------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------

response.menu += [
            (T('Altas'), False, URL('default','index'), [
                (T('Clientes'), False, URL('altas', 'alta_cliente'),[]),
                (T('proveedores'), False, URL('altas', 'alta_proveedor'),[]),
                (T('empleados'), False, URL('altas', 'alta_empleado'),[]),
                (T('ventas'), False,URL('altas', 'alta_venta'),[])])]

#-------------------------------------
response.menu += [
            (T('Reportes'), False, URL('default','index'), [
                (T('Clientes'), False, URL('reportes', 'ReportesClientes'),[]),
                (T('Empleados'), False, URL('reportes', 'ReportesEmpleados'),[]),
                (T('Productos'), False, URL('reportes', 'ReportesProductos'),[]),
                (T('Proveedores'), False, URL('reportes', 'ReportesProveedores'),[])])]
#-------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------
response.menu+=[(T('Consultas'),False,'#',
                 [(T('Clientes'),False,'#',
                   [(T('Por Ciudad'),False,URL(request.application,'consultas','ClientesPorCiudad'),[]),
                    (T('Por DNI'),False,URL(request.application,'consultas','ClientesPorDni'),[]),
					(T('Por Apellido'),False,URL(request.application,'consultas','ClientesPorApellido'),[])],),

                  (T('Proveedores'),False,'#',
                   [(T('Por Cuit'),False,URL(request.application,'consultas','ProveedorPorCuit'),[]),
                    (T('Por Nombre'),False,URL(request.application,'consultas','ProveedorPorNombre'),[])],),

				(T('Producto'),False,'#',
                   [(T('Por Categoria'),False,URL(request.application,'consultas','ProductoPorCategoria'),[]),
					(T('Por Codigo'),False,URL(request.application,'consultas','ProductoPorCodigo'),[]),
                    (T('Por Nombre'),False,URL(request.application,'consultas','ProductoPorNombre'),[])],),


                  (T('Empleados'),False,'#',
                   [(T('Por Legajo'),False,URL(request.application,'consultas','Empleadosporlegajo'),[]),
                    (T('Por DNI'),False,URL(request.application,'consultas','Empleadospordni'),[]),],),
                 ],
                   )]
#---------------------------------------------------------------------------------------------------------------------------------------

response.menu += [
            (T('Compras'), False, URL('default','index'), [
                (T('Proveedores'), False, URL('compras', 'ComprasProveedores'),[])])]
#------------------------------------------------------------------------------------------------------------------------------------02-05-17

#---------------------------------------------------------------------------------------------------------------------------------------

response.menu += [
            (T('Ventas'), False, URL('default','index'), [
                (T('Ventas Local'), False, URL('ventas', 'VentasLocal'),[])])]
#------------------------------------------------------------------------------------------------------------------------------------02-05-17
