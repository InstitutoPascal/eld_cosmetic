# -*- coding: utf-8 -*-
def ClientesPorCiudad():
    subtitulo=T('Ingrese la Ciudad del Cliente a buscar:')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("",INPUT(_type="text",_name="ciudad",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar",_class="btn btn-primary"))))#construlle el formulario para la vista, submit (tipo boton)```
    if form.accepts(request.vars,session):
        ### verifica si la carrera está en la base de datos
        #if db(db.clientes.localidad_cliente!=form.vars.ciudad).count()==0:
        if db(db.clientes.localidad_cliente!=form.vars.localidad_cliente).count()==0:
            form.errors.codigo="El nombre ingresado no está en la base de datos"
            response.flash = 'El nombre ingresado no está en la base de datos'
        else:
          
            listado =db(db.clientes.localidad_cliente==form.vars.ciudad).select(db.clientes.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('DNI',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('APELLIDO',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('NOMBRE',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' CLIENTE',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
            *[TR(TD(rows.dni,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(rows.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(rows.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for rows in listado]),)) #rows recorre el contenido del listado y con el for cuenta la cantidad
            tablaFinal = DIV(lista)
            
            
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Por favor, complete el Formulario'

    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)



#------------------------------------------------------------------------------------------
#Busqueda por Apellido

#def index(): return dict(message="hello from listados.py")

def ClientesPorApellido():
    subtitulo=T('Ingrese el apellido del cliente a buscar:')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("",INPUT(_type="text",_name="apellido",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar",_class="btn btn-primary"))))#construlle el formulario para la vista, submit (tipo boton)
    if form.accepts(request.vars,session):
        ### verifica si la carrera estÃ¡ en la base de datos
        if db(db.clientes.apellido==form.vars.apellido).count()==0: #este count cuenta los registros y si es == a 0 muestra el error
            form.errors.codigo="El apellido ingresado no esta en la base de datos"
            response.flash = 'El apellido ingresado no esta en la base de datos'
        else:
          
            listado =db(db.clientes.apellido==form.vars.apellido).select(db.clientes.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('DNI',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('APELLIDO',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('NOMBRE',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' CLIENTE',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
            *[TR(TD(x.dni,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(x.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            
            
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Por favor, complete el Formulario'

    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)

#-------------------------------------------------------------------------------------------------------------
#busqueda por dni
#def index(): return dict(message="hello from listados.py")

def ClientesPorDni():
    subtitulo=T('Ingrese el DNI del cliente a buscar')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("",INPUT(_type="integer",_name="dni",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar",_class="btn btn-primary"))))#construlle el formulario para la vista, submit (tipo boton)
    if form.accepts(request.vars,session):
        ### verifica si la carrera estÃ¡ en la base de datos
        if db(db.clientes.dni==form.vars.dni).count()==0: #este count cuenta los registros y si es == a 0 muestra el error
            form.errors.codigo="El dni ingresado no esta en la base de datos"
            response.flash = 'El dni ingresado no esta en la base de datos'
        else:
          
            listado =db(db.clientes.dni==form.vars.dni).select(db.clientes.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('DNI',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('APELLIDO',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('NOMBRE',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' CLIENTE',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
            *[TR(TD(x.dni,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(x.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            
            
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Por favor, complete el Formulario'

    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)
# ------------------------------------------------------------------------------------------------------------------------------------------
# busqueda de proveedor por cuit
#ProveedorPorCuit():
def ProveedorPorCuit():
    subtitulo=T('Ingrese el Cuit del proveedor a buscar:')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("",INPUT(_type="text",_name="cuit_proveedor",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar",_class="btn btn-primary"))))#construlle el formulario para la vista, submit (tipo boton)
    if form.accepts(request.vars,session):
        ### verifica si la carrera estÃ¡ en la base de datos
        if db(db.proveedor.cuit_proveedor==form.vars.cuit_proveedor).count()==0: #este count cuenta los registros y si es == a 0 muestra el error
            form.errors.codigo="El dni ingresado no esta en la base de datos"
            response.flash = 'El dni ingresado no esta en la base de datos'
        else:
          
            listado =db(db.proveedor.cuit_proveedor==form.vars.cuit_proveedor).select(db.proveedor.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('Cuit',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Nombre',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Telefono',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' CLIENTE',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
            *[TR(TD(x.cuit_proveedor,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(x.nombre_empresa,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.telefono,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            
            
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Por favor, complete el Formulario'

    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)
#-------------------------------------------------------------------------------------------------
# busqueda de proveedor por nombre
#def ProveedorPorNombre():

def ProveedorPorNombre():
    subtitulo=T('Inrese el nombre de proveedor a buscar:')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("",INPUT(_type="text",_name="dni",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar",_class="btn btn-primary"))))#construlle el formulario para la vista, submit (tipo boton)
    if form.accepts(request.vars,session):
        ### verifica si la carrera estÃ¡ en la base de datos
        if db(db.proveedor.nombre_empresa==form.vars.nombre_empresa).count()==0: #este count cuenta los registros y si es == a 0 muestra el error
            form.errors.codigo="El nombre ingresado no esta en la base de datos"
            response.flash = 'El nombre ingresado no esta en la base de datos'
        else:
          
            listado =db(db.proveedor.nombre_empresa==form.vars.nombre_empresa).select(db.proveedor.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('DNI',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('APELLIDO',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('NOMBRE',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' CLIENTE',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
            *[TR(TD(x.dni,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(x.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            
            
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Por favor, complete el Formulario'

    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)

#--------------------------------------------------------------------------------------
def Empleadosporlegajo():
    subtitulo=T('Ingrese el numero de legajo de empleado a buscar:')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("",INPUT(_type="integer",_name="codigo_empleados",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar",_class="btn btn-primary"))))#construlle el formulario para la vista, submit (tipo boton)
    if form.accepts(request.vars,session):
        ### verifica si la carrera estÃ¡ en la base de datos
        if db(db.empleados.codigo_empleados==form.vars.codigo_empleados).count()==0: #este count cuenta los registros y si es == a 0 muestra el error
            form.errors.codigo_empleados="El LEGAJO ingresado no esta en la base de datos"
            response.flash = 'El LEGAJO ingresado no esta en la base de datos'
        else:
          
            listado =db(db.empleados.codigo_empleados==form.vars.codigo_empleados).select(db.empleados.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('DNI',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('APELLIDO',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('NOMBRE',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' CLIENTE',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
            *[TR(TD(x.dni,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(x.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            
            
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Por favor, complete el Formulario'

    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)
#--------------------------------------------------------------------------------------------------------------------
def Empleadospordni():
    subtitulo=T('Ingrese el DNI del empleado a buscar:')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("",INPUT(_type="integer",_name="dni",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar",_class="btn btn-primary"))))#construlle el formulario para la vista, submit (tipo boton)
    if form.accepts(request.vars,session):
        ### verifica si la carrera estÃ¡ en la base de datos
        if db(db.empleados.dni==form.vars.dni).count()==0: #este count cuenta los registros y si es == a 0 muestra el error
            form.errors.dni="El dni ingresado no esta en la base de datos"
            response.flash = 'El dni ingresado no esta en la base de datos'
        else:
          
            listado =db(db.empleados.dni==form.vars.dni).select(db.empleados.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('DNI',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('APELLIDO',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('NOMBRE',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' CLIENTE',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
            *[TR(TD(x.dni,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(x.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            
            
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Por favor, complete el Formulario'

    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)
#------------------------------------------------------------------------------------------------------
# Producto por categoria
def ProductoPorCategoria():
    subtitulo=T('Ingrese la categoria de producto a buscar:')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("",INPUT(_type="text",_name="categoria",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar",_class="btn btn-primary"))))#construlle el formulario para la vista, submit (tipo boton)
    if form.accepts(request.vars,session):
        ### verifica si la carrera está en la base de datos
        #if db(db.clientes.localidad_cliente!=form.vars.ciudad).count()==0:
        if db(db.categorias_prod.categoria!=form.vars.categoria).count()==0:
            form.errors.codigo="El nombre ingresado no está en la base de datos"
            response.flash = 'El nombre ingresado no está en la base de datos'
        else:
          
            listado =db(db.categorias_prod.categoria==form.vars.categoria).select(db.categorias_prod.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('DNI',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('APELLIDO',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('NOMBRE',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' CLIENTE',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
            *[TR(TD(rows.dni,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(rows.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(rows.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for rows in listado]),)) #rows recorre el contenido del listado y con el for cuenta la cantidad
            tablaFinal = DIV(lista)
            
            
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Por favor, complete el Formulario'

    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)

#--------------------------------------------------------------------------------------------------------------------
# consulta por producto por nombre

def ProductoPorNombre():
    subtitulo=T('Ingrese el nombre por producto a buscar')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("",INPUT(_type="text",_name="nombre",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar",_class="btn btn-primary"))))#construlle el formulario para la vista, submit (tipo boton)
    if form.accepts(request.vars,session):
        ### verifica si la carrera estÃ¡ en la base de datos
        if db(db.productos.nombre==form.vars.nombre).count()==0: #este count cuenta los registros y si es == a 0 muestra el error
            form.errors.nombre="El nombre ingresado no esta en la base de datos"
            response.flash = 'El nombre ingresado no esta en la base de datos'
        else:
          
            listado =db(db.productos.nombre==form.vars.nombre).select(db.productos.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('Codigo producto',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Nombre',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Marca',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Categoria',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'), TH('Precio',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'), TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),)),
            *[TR(TD(x.codigo_producto,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(x.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.marca,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.categoriaP,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'), TD(x.precio,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            
            
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Por favor, complete el Formulario'

    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)

#--------------------------------------------------------------------------------------------------------------------
#Producto por codigo

def ProductoPorCodigo():
    subtitulo=T('Ingrese su codigo de producto a buscar:')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("",INPUT(_type="text",_name="codigo",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar",_class="btn btn-primary"))))#construlle el formulario para la vista, submit (tipo boton)
    if form.accepts(request.vars,session):
        ### verifica si la carrera está en la base de datos
        #if db(db.clientes.localidad_cliente!=form.vars.ciudad).count()==0:
        if db(db.codigo_producto.codigo!=form.vars.codigo).count()==0:
            form.errors.codigo="El nombre ingresado no está en la base de datos"
            response.flash = 'El nombre ingresado no está en la base de datos'
        else:
          
            listado =db(db.codigo_producto.codigo==form.vars.codigo).select(db.codigo_producto.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('DNI',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('APELLIDO',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('NOMBRE',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' CLIENTE',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
            *[TR(TD(rows.dni,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(rows.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(rows.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for rows in listado]),)) #rows recorre el contenido del listado y con el for cuenta la cantidad
            tablaFinal = DIV(lista)
            
            
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Por favor, complete el Formulario'

    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)

#--------------------------------------------------------------------------------------------------------------------
