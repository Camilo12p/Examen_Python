import os 
import modulos.coreFile as core
from tabulate import tabulate

def opciones(context:str,titulo:str='',titulo2:str='',titulo3:str='')->int:  #validacion de las opciones que solo ingresen numeros >=0
    core.clearScreen()
    print(titulo)
    print(titulo2)
    print(titulo3)                
    try:
        n= int(input(f'{context} --> ' ))
        if n>=0:
            return n
        else:
            return opciones(context,titulo,titulo2,titulo3)    
    except ValueError:
        return opciones(context,titulo,titulo2,titulo3)

def flotantes(context:str)->str:  #funcion que valida que solo se ingrese numeros >=0
    core.clearScreen()
    try:
        n=float(input(f'{context} --> ' ))
        if n>=0:
            return n
        else:
            return flotantes(context)    
    except ValueError:
        return flotantes(context)

def enteros(context:str)->int:  #funcion que valida que solo sean enteros >=0
    core.clearScreen()
    try:
        n= int(input(f'{context} --> ' ))
        if n>=0:
            return n
        else:
            return enteros(context)    
    except ValueError:
        return enteros(context)

def cadenas(context:str)->str:   #funcion que solo recibe cadenas de texto sin ningun numero 
    core.clearScreen()
    n=str(input(f'{context} --> ')).split(' ')
    for items in n:
        if not items.isalpha():
            return cadenas(context)
    return ' '.join(n)

def direccion(context:str)->str:   #validar direccion falta mejorar
    core.clearScreen()
    dir=str(input(f'{context} --> '))
    return dir

def email(context:str)->str:  #valida el email que contenga almenos un @
    core.clearScreen()
    n=str(input(f'{context} --> '))
    if n.isalpha():
        return email(context)
    return n

def newRegister(nameFile:str)->int:  #valida si el id ya se encuentra registrado
    core.clearScreen()
    data={}
    data.update(core.readFile(nameFile))

    n = enteros('Ingrese el ID')
    if str(n) in data:  # valida que el id no este en el sistema
        print('El id ya se encuentra registrado')
        core.pauseScreen()
        return newRegister(nameFile)
    return n

def cargo()->str:   #valida el cargo que contiene la persona 
    titulo='Que tipo de cargo tiene el empleado'
    cargos=['Almacenista','Jefe','IT','Administrador','Mensajero','Gerente']
    menu=[['1. Almacenista'],['2. Jefe'],['3. IT'],['4. Administrador'],['5. Mensajero'],['6. Gerente']]
    op= opciones('Ingrese la opcion',titulo,tabulate(menu,tablefmt='fancy-grid'))

    if op>0 and op<=6:  #valida que se elija la respuesta correcta
        return cargos[op-1]
    else:
        return cargo()  

def newEmploye(nameFile)->int:  #valida que el empleado se encuentre en el sistema
    core.clearScreen()
    data={}
    data.update(core.readFile(nameFile).get('employes'))

    n = enteros('Ingrese el ID')
    if str(n) in data:  # valida que el id no este en el sistema
        print('El id ya se encuentra registrado')
        core.pauseScreen()
        return newEmploye(nameFile)
    else:
        return n
        

def Employe(nameFile)->int:  #valida que el empleado se encuentre en el sistema
    core.clearScreen()
    data={}
    data.update(core.readFile(nameFile).get('employes'))

    n = enteros('Ingrese el ID')
    if str(n) in data:  # valida que el id no este en el sistema
        return n
    else:     
        print('El id no se encuentra registrado')
        core.pauseScreen()
        return Employe(nameFile)

def pays(nameFile)->int:  #valida si hay pagos 
    core.clearScreen()
    data={}
    data.update(core.readFile(nameFile).get('pays'))

    n = enteros('Ingrese el ID')
    if str(n) in data:  # valida que el id no este en el sistema
        return n
    else:     
        print('no hay pagos registrados para ese id')
        core.pauseScreen()
        return pays(nameFile)


def diasTrabajados():  #valida los dias trabajados
    n=flotantes('Ingrese los dias trabajados')  #llama a la funcion que solo recibe numeros mayores que cero
    if n<=31:   #valida que nadie supere los 31 dias
        return n
    else:
        return diasTrabajados()