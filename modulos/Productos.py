import modulos.coreFile as core
import modulos.validate as v


def Productos():
    #SE LEE EL JSON PARA TENER LA INFO MAS ACTUALIZADA
    Productos={}
    Productos.update(core.readFile('Ejercicio3.json'))
    #SE LE HACE LAS PETICIONES AL USUAROP
    id= v.newRegister('Ejercicio3.json')
    nombre=v.cadenas('Ingrese el nombre del producto')
    valorU=v.flotantes('Ingrese el valor unitario del producto')
    stockMin=v.enteros('Ingrese el stock minimo')
    stockMax=v.enteros('Ingrese el stock maximo')

    #SE PONE EN UN DICCIONARIO
    producto={
        'id':id,
        'nombre':nombre,
        'valorUnitario':valorU,
        'stockMin':stockMin,
        'stockMax':stockMax
    }
    # SE ACTUALIZA EL JSON Y EL DICCIONARIO INTERNO 
    Productos.update({id:producto})
    core.updateFile('Ejercicio3.json',Productos)