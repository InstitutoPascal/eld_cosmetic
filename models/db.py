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
#auth.define_tables(username=False, signature=False)

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
"""
##Localidad##
#db.define_table ('localidad',
  #               db.Field ('cp','integer'),
   #              db.Field ('nombre_localidad','string'),
         #                 )
db.localidad.cp.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.localidad.nombre_localidad.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')  """

##Clientes##
db.define_table ('clientes',
                 db.Field ('codigo_cliente','integer'),
                 db.Field ('nombre','string'),
                 db.Field ('apellido','string'),
                 db.Field ('dni','integer',unique=True),
                 #db.Field ('sexo'),
                 db.Field('telefono','integer'),
                 #db.Field ('password','password'),
                 db.Field ('localidad_cliente','string'),)
db.clientes.codigo_cliente.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres')
db.clientes.nombre.requires=IS_NOT_EMPTY()
db.clientes.nombre.requires=IS_UPPER()
db.clientes.nombre.requires=IS_LENGTH(14)
db.clientes.apellido.requires=IS_NOT_EMPTY()
db.clientes.apellido.requires=IS_UPPER()
db.clientes.apellido.requires=IS_LENGTH(14)
db.clientes.dni.requires=IS_NOT_IN_DB (db,db.clientes.dni)
db.clientes.dni.requires=IS_INT_IN_RANGE(2500000,100000000)
db.clientes.localidad_cliente.requires=IS_UPPER()
db.clientes.localidad_cliente.requires=IS_LENGTH(20)
db.clientes.localidad_cliente.requires=IS_NOT_EMPTY(error_message='Campo obligatorio')

#db.clientes.localidad_Cliente.requires=IS_IN_DB(db,db.localidad),'%(nombre_localidad)s'
#db.clientes.sexo.requires=IS_IN_SET (['Masculino','Femenino'])





##Proveedor##
db.define_table('proveedor',
                 #db.Field('codigo_proveedor','integer'),
                 db.Field('nombre_empresa','string'),
                 db.Field('cuit_proveedor','string'),
                 db.Field('localidad','string'),
                 db.Field('direccion','string'),
                 db.Field('numero_calle','integer'),
                 db.Field('telefono','integer'),
                 db.Field('email','string'))
#db.proveedor.codigo_proveedor.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres')
db.proveedor.localidad.requires=IS_NOT_EMPTY(error_message='Campo obligatorio')
db.proveedor.telefono.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')
db.proveedor.email.requires=IS_LENGTH(30, error_message='Solo hasta 30 caracteres')
db.proveedor.nombre_empresa.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')
db.proveedor.cuit_proveedor.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(13, error_message='Solo hasta 13 caracteres')
db.proveedor.direccion.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')
db.proveedor.numero_calle.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(6, error_message='Solo hasta 6 caracteres')


##Categoria##
db.define_table ('categorias_prod',
                 db.Field('categoria','string'),
                 primarykey=['categoria'] )
db.categorias_prod.categoria.requires=IS_UPPER(),IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(8, error_message='Solo hasta 8 caracteres')

##Productos#
db.define_table ('productos',
                 db.Field('codigo_producto','string'),
                 db.Field ('nombre','string'),
                 db.Field ('marca','string'),
                 #db.Field ('numart','integer',unique=True),
                 ###db.Field ('categoriaP','string'),
                 #db.Field ('categoriaP','string'),
                 #db.Field('cantidad_prod','integer'),
                 #db.Field ('categoria','string'),
                 db.Field('precio','integer'),
                 #db.Field('fecha_venta','string'),
                 db.Field('proveedor',db.proveedor)
                 #db.Field('fecha_compra','string'
                )


#db.productos.cantidad_prod.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(6, error_message='Solo hasta 6 caracteres')
#db.productos.categoria.requires=IS_UPPER(),IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres')

#db.productos.categoriaP.requires=IS_IN_DB(db,db.categorias_prod.categoria,) #Subconsulta a la tablacategorias_prod campo categoria
#db.productos.categoriaP.requires=IS_IN_DB(db,db.categorias_prod,'%(categoria)s',) #Subconsulta a la tablacategorias_prod campo categoria

#db.productos.categoriaP.requires=IS_IN_DB(db,db.categorias_prod.id,'%(categoria)s') #Subconsulta a la tablacategorias_prod campo categoria

db.productos.precio.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(6, error_message='Solo hasta 6 caracteres')
#db.productos.fecha_venta.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
#db.productos.fecha_compra.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')

########db.productos.proveedor.requires=IS_IN_DB(db,db.proveedor,'%(nombre_empresa)s',) #subconsulta que obtiene datos de la tabla proveedor y campo codigo_proveedor
#,'%(field)s'  #permite mostrar el valor de un campo para que sea mas facil identificarlo 



db.productos.codigo_producto.requires=IS_UPPER(),IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(9, error_message='Solo hasta 9 caracteres',)
db.productos.nombre.requires=IS_UPPER(),IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')





##Empleados##
db.define_table('empleados',
                db.Field('codigo_empleados','integer'),
                db.Field('dni','integer',unique=True),
                db.Field('apellido','string'),
                db.Field('nombre','string'),
                db.Field('usuario','string'),
                db.Field('password','password'))
db.empleados.codigo_empleados.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres')
db.empleados.dni.requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio') ,IS_INT_IN_RANGE(2500000,100000000, error_message= 'Ingrese un DNI entre 2.500.000 y 100.000.000')
db.empleados.apellido.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.empleados.nombre.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.empleados.usuario.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.empleados.password.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(15, error_message='Solo hasta 15 caracteres')

##stock##
db.define_table ('stock',
                 db.Field('codigo_producto','string'),
                 db.Field ('nombre','string'),
                 db.Field ('marca','string'),
                 db.Field ('categoria','string'),
                 db.Field('fecha_ingreso','string'),
                 db.Field('fecha_salida','string'))


db.stock.categoria.requires=IS_UPPER(),IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres')
#db.productos.precio.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(6, error_message='Solo hasta 6 caracteres')
db.stock.fecha_ingreso.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.stock.fecha_salida.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.stock.marca.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.stock.codigo_producto.requires=IS_UPPER(),IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(9, error_message='Solo hasta 9 caracteres',)
db.stock.nombre.requires=IS_UPPER(),IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')

#---------------------------------------------------------------------------------------------------------------------------------------------06/04/2017
# ventas #
db.define_table ('ventas',
                 db.Field('codigo_producto','string'),
                 db.Field ('nombre','string'),
                 db.Field ('marca','string'),
                 db.Field ('categoria','string'),
                 #db.Field ('precio','int'),
                 db.Field('fecha_ingreso','string'),
                 db.Field('fecha_salida','string'))


db.ventas.categoria.requires=IS_UPPER(),IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(4, error_message='Solo hasta 4 caracteres')
#db.ventas.precio.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(6, error_message='Solo hasta 6 caracteres')
db.ventas.fecha_ingreso.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.ventas.fecha_salida.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.ventas.marca.requires=IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
db.ventas.codigo_producto.requires=IS_UPPER(),IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(9, error_message='Solo hasta 9 caracteres',)
db.ventas.nombre.requires=IS_UPPER(),IS_NOT_EMPTY(error_message='Campo obligatorio'),IS_LENGTH(10, error_message='Solo hasta 10 caracteres')
