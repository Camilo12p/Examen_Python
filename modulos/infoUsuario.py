import modulos.coreFile as core
import modulos.validate as v

def addUser():

    # TODO LO QUE SE LE PUEDE PEDIR AL USUARIO
    Users={}
    id= v.enteros('Ingrese el valor del usuario')
    nombres=v.cadenas('Ingrese el nombre de la persona')
    apellidos=v.cadenas('Ingrese el apellido de la persona')
    dir=v.direccion('Ingrese la direccion')
    ciudad=v.cadenas('Ingrese la ciudad')
    longitud=v.flotantes('Ingrese la longitud')
    latitud=v.flotantes('Ingrese la latitud')
    email=v.email('Ingrese el email')
    edad=v.enteros('Ingrese la edad')
    ocupacion=v.cadenas('Ingrese la ocupacion')

    user={
        'id':id,
        'name':nombres,
        'apellidos':apellidos,
        'ubicacion':{
            'direccion':dir,
            'ciudad':ciudad,
            'longitud':longitud,
            'latitud':latitud,
        },
        'email':email,
        'edad':edad,
        'ocupacion':ocupacion
    }

    # SE ACTUALIZA EL USUARIO E IMPRIME
    Users.update({id:user})
    for key,value in user.items():
        print(f'{key}: {value}')
    core.pauseScreen()