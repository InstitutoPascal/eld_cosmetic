# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.14.1":
    raise HTTP(500, "Requires web2py 2.13.3 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# app configuration made easy. Look inside private/appconfig.ini
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
myconf = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    db = DAL(myconf.get('db.uri'),
             pool_size=myconf.get('db.pool_size'),
             migrate_enabled=myconf.get('db.migrate'),
             check_reserved=['all'])
else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = ['*'] if request.is_local else []
# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = myconf.get('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.get('forms.separator') or ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

from gluon.tools import Auth, Service, PluginManager

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=myconf.get('host.names'))
service = Service()
plugins = PluginManager()

# -------------------------------------------------------------------------
# create all tables needed by auth if not custom tables
# -------------------------------------------------------------------------
auth.define_tables(username=False, signature=False)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.get('smtp.server')
mail.settings.sender = myconf.get('smtp.sender')
mail.settings.login = myconf.get('smtp.login')
mail.settings.tls = myconf.get('smtp.tls') or False
mail.settings.ssl = myconf.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)


##Clientes##
db.define_table ('clientes',
                 db.Field("id_clientes","id"),  #agregada by enrique
                 db.Field ('codigo_cliente','integer'),
                 db.Field ('nombre','string'),
                 db.Field ('apellido','string'),
                 db.Field ('email','string'),  #agregada by enrique
                 db.Field ('dni','integer',unique=True),
                 db.Field('cuil','string'),
                 db.Field('sexo', requires=IS_IN_SET(['Masculino', 'Femenino', 'Otro'])),
                 db.Field('telefono','integer'),
                 db.Field('direccion','string'),
                 db.Field('localidad_cliente','string'),
                 db.Field('tipo_categoria', requires=IS_IN_SET(['Resp. Inscr.','Monotributo'])),  #agregada by enrique
                 db.Field ('provincia','string'),
                 db.Field ('pais','string'),
                 db.Field ('codigo_postal','integer'),
                 db.Field('estado', requires=IS_IN_SET(['activo','inactivo'])),
                 db.Field ('observaciones','text')
                )
db.clientes.codigo_cliente.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres'),IS_NOT_IN_DB (db,db.clientes.codigo_cliente)
db.clientes.nombre.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_UPPER(),IS_LENGTH(30)
db.clientes.apellido.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_UPPER(),IS_LENGTH(30)
db.clientes.dni.requires=IS_NOT_IN_DB (db,db.clientes.dni),IS_INT_IN_RANGE(2500000,100000000)
db.clientes.telefono.requires=IS_LENGTH(12, error_message='Solo hasta 12 caracteres')
#db.clientes.localidad_cliente.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_UPPER(),IS_LENGTH(50),IS_IN_DB(db,'localidad.nombre_localidad','%(nombre_localidad)s')
#db.clientes.direccion.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_UPPER(),IS_LENGTH(20)
#db.clientes.numero_calle.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(8, error_message='Solo hasta 8 caracteres')
db.clientes.provincia.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_UPPER()
db.clientes.pais.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_UPPER()
db.clientes.codigo_postal.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(8, error_message='Solo hasta 8 caracteres')


#db.clientes.localidad_Cliente.requires=IS_IN_DB(db,db.localidad),'%(nombre_localidad)s'
#db.clientes.sexo.requires=IS_IN_SET (['Masculino','Femenino'])

db.define_table('localidad',
                db.Field('nombre_localidad','string'),
                db.Field('codigo_postal','integer'))

##Proveedor##
db.define_table('proveedor',
                 db.Field('codigo_proveedor','integer'),
                 db.Field('nombre_empresa','string'),
                 db.Field('cuit_proveedor','string'),
                 db.Field('direccion','string'),
                 db.Field('codigo_postal','integer'),
                 db.Field('localidad','string'),
                 db.Field('provincia','string'),
                 db.Field('pais','string'),
                 db.Field('telefono','integer'),
                 db.Field('email','string'),
                 db.Field('razon_social','string'),
                 db.Field('fecha_registro','string'),
                 db.Field('pagina_web','string'),
                 db.Field('estado',requires=IS_IN_SET(['activo','inactivo'])),
                 db.Field('observaciones','text')
               )
db.proveedor.codigo_proveedor.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres')
db.proveedor.nombre_empresa.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_UPPER()
db.proveedor.cuit_proveedor.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(18, error_message='Solo hasta 13 caracteres')
db.proveedor.direccion.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(30, error_message='Solo hasta 15 caracteres')
db.proveedor.codigo_postal.requires=IS_LENGTH(5, error_message='Solo hasta 5 caracteres')
db.proveedor.localidad.requires=IS_NOT_EMPTY(error_message='Campo obligatorio')
db.proveedor.provincia.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(30, error_message='Solo hasta 10 caracteres')
db.proveedor.pais.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(20, error_message='Solo hasta 20 caracteres')
db.proveedor.telefono.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')
db.proveedor.email.requires=IS_LENGTH(30, error_message='Solo hasta 30 caracteres')
db.proveedor.razon_social.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')
db.proveedor.fecha_registro.requires=IS_NOT_EMPTY(error_message='Campo obligatorio')
db.proveedor.pagina_web.requires=IS_LENGTH(30, error_message='Solo hasta 30 caracteres')

##Categoria##

#db.define_table ('categorias',
#                db.Field('categoria','string'),
#                 primarykey=['categoria'] )
#db.categorias_prod.categoria.requires=IS_UPPER(),IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(8, error_message='Solo hasta 8 caracteres')


##Productos#
db.define_table ('productos',
                 db.Field("id_producto","id"),  #agregada by enrique
                 #db.Field('id','integer'),
                 db.Field('codigo_barras', 'string'),
                 db.Field('cantidad_prod','integer'),
                 db.Field ('nombre','string'),
                 db.Field ('marca','string'),
                 db.Field('descripcion','string'),
                 db.Field('envase','string'),
                 db.Field ('categoria','string'),
                 db.Field('precio','float'),
                 db.Field('proveedor','string'),
                 db.Field ('codigo_producto','string'),
                 db.Field ('fecha_ingreso','string'),
                 db.Field('numero_remito','integer'),
                 db.Field('numero_lote','integer'),
                 db.Field('imagen','upload'),
                 db.Field('observaciones','text'),
                 db.Field('alicuota_iva','float') #agregada by enrique
                 )


db.productos.codigo_producto.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(9, error_message='Solo hasta 9 caracteres'), IS_NOT_IN_DB(db,db.productos.codigo_producto)
db.productos.cantidad_prod.requires=IS_NOT_EMPTY(error_message='Campo obligatorio')
db.productos.nombre.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(20, error_message='Solo hasta 20 caracteres'),IS_UPPER()
db.productos.marca.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_UPPER()
db.productos.categoria.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(16, error_message='Solo hasta 16 caracteres'),IS_UPPER()
db.productos.precio.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(6, error_message='Solo hasta 6 caracteres')
db.productos.proveedor.requires=IS_IN_DB(db,db.proveedor,'%(nombre_empresa)s',) #subconsulta que obtiene datos de la tabla proveedor y campo codigo_proveedor
#,'%(field)s'  #permite mostrar el valor de un campo para que sea mas facil identificarlo 
db.productos.fecha_ingreso.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.productos.numero_lote.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.productos.observaciones.requires=IS_LENGTH(200, error_message='Solo hasta 200 caracteres')








##Empleados##
db.define_table('empleados',
                db.Field('usuario_id', db.auth_user, default=auth.user_id ),
                db.Field('codigo_empleados','integer'),
                db.Field('dni','integer'),
                db.Field('apellido','string'),
                db.Field('nombre','string'),
                db.Field('cuil','string'),
                db.Field('usuario','string'),
                db.Field('password','password'),
                db.Field('email','string'),
                db.Field('direccion', 'string'),
                db.Field('localidad','string'),
                db.Field('codigo_postal','integer'),
                db.Field('provincia','string'),
                db.Field('pais','string'),
                db.Field('telefono','string'),
                db.Field('fecha_ingreso','date'),
                db.Field('estado', requires=IS_IN_SET(['activo','inactivo'])),
                db.Field('cargo','string'),
                db.Field('sector','string'),)

db.empleados.codigo_empleados.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres'),IS_NOT_IN_DB (db,db.empleados.codigo_empleados)
db.empleados.dni.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio') ,IS_INT_IN_RANGE(2500000,100000000, error_message= 'Ingrese un DNI entre 2.500.000 y 100.000.000')
db.empleados.apellido.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(30, error_message='Solo hasta 30 caracteres'),IS_UPPER()
db.empleados.nombre.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(30, error_message='Solo hasta 30 caracteres'),IS_UPPER()
db.empleados.usuario.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(30, error_message='Solo hasta 30 caracteres')
db.empleados.password.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')
db.empleados.email.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(50, error_message='Solo hasta 50 caracteres')
db.empleados.direccion.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(50, error_message='Solo hasta 50 caracteres'),IS_UPPER()
db.empleados.localidad.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(50, error_message='Solo hasta 50 caracteres')
db.empleados.codigo_postal.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(6, error_message='Solo hasta 6 caracteres')
db.empleados.provincia.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(30,error_message='Solo hasta 30 caracteres')
db.empleados.pais.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(20, error_message='Solo hasta 20 caracteres')
db.empleados.telefono.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(20, error_message='Solo hasta 20 caracteres')
db.empleados.fecha_ingreso.requires=IS_NOT_EMPTY(error_message='Campo obligatorio')
db.empleados.sector.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(20, error_message='Solo hasta 20 caracteres')

##stock##
db.define_table ('stock',
                 db.Field('codigo_producto','string'),
                 db.Field ('nombre','string'),
                 db.Field ('marca','string'),
                 db.Field ('categoria','string'),
                 db.Field('fecha_ingreso','string'),
                 db.Field('fecha_salida','string'))


db.stock.categoria.requires=IS_UPPER(),IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres')
db.stock.fecha_ingreso.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.stock.fecha_salida.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.stock.marca.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.stock.codigo_producto.requires=IS_UPPER(),IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(9, error_message='Solo hasta 9 caracteres',)
db.stock.nombre.requires=IS_UPPER(),IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')

#---------------------------------------------------------------------------------------------------------------------------------------------06/04/2017
#___________________________________________________________________________________________________________________________________________________________
db.define_table ('compras',
                 db.Field('codigo_producto','string'),
                 db.Field ('nombre','string'),
                 db.Field ('marca','string'),
                 db.Field ('categoria','string'),
                 db.Field ('precio','integer'),
                 db.Field('fecha_ingreso','string'),
                 #db.Field('fecha_salida','date'),
                 db.Field('proveedor','string'),
                 db.Field('remito','string'),
                 db.Field('cantidad','integer')
                )
db.compras.codigo_producto.requires=IS_UPPER(),IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.compras.nombre.requires=IS_UPPER(),IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(30, error_message='Solo hasta 30 caracteres')
db.compras.marca.requires=IS_UPPER(),IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(30, error_message='Solo hasta 30 caracteres')
db.compras.categoria.requires=IS_UPPER(),IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres')
db.compras.precio.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(6, error_message='Solo hasta 6 caracteres')
db.compras.fecha_ingreso.requires=IS_NOT_EMPTY(error_message='Campo obligatorio')
#db.compras.fecha_salida.requires=IS_NOT_EMPTY(error_message='Campo obligatorio')
db.compras.cantidad.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.compras.proveedor.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(130, error_message='Solo hasta 10 caracteres')
db.compras.remito.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
#db.compras.factura.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
#db.compras.orden_compra.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')


#---------------------------------------------------------------------------------------------------------------------------------------------------------------
