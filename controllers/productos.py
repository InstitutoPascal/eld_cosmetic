def index():
    regs = db(db.productos.id>0).select()
    

    form=FORM(TABLE(TR("",INPUT(_type="text",_name="ciudad",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar",_class="btn btn-primary"))))#construlle el formulario para la vista, submit (tipo boton)```
    if form.accepts(request.vars,session):
        ### verifica si la carrera está en la base de datos
        #if db(db.clientes.localidad_cliente!=form.vars.ciudad).count()==0:
        if db(db.clientes.localidad_cliente!=form.vars.localidad_cliente).count()==0:
            form.errors.codigo="El nombre ingresado no está en la base de datos"
            response.flash = 'El nombre ingresado no está en la base de datos'
        else:
          
            listado =db(db.clientes.localidad_cliente==form.vars.ciudad).select(db.clientes.ALL)
    return dict(form=form,productos=regs)
def ver():
   # obtengo el id de prodcuto desde la URL
    prod_id = request.args[0]
   # consultamos a la bd para que traiga el registro del primer producto:
    reg = db(db.productos.id==prod_id).select().first()
    return dict(productos=reg)

def mostrar():
    # obtengo el id de prodcuto desde la URL
    prod_id = request.args[0]
    # consultamos a la bd para que traiga el registro del primer producto:
    reg = db(db.productos.id==prod_id).select(db.productos.image).first()
    # obtenemos la imagen (nombre de archivo completo, stream=flujo de datos=archivo abierto -open-):
    (filename, stream) = db.productos.image.retrieve(reg.image)
    # obtenemos extension original para determinar tipo de contenido:
    import os.path
    ext = os.path.splitext(filename)[1].lower()
    if ext in (".jpg", ".jpeg", ".face"):
        formato = "image/jpeg"
    elif ext in (".png"):
        formato = "image/png"
    response.headers['Content-Type'] = formato
    # devolver al navegador el contenido de la imagen
    return stream
