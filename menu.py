from tabulate import tabulate
import modulos.coreFile as core
import modulos.conversion as c
import modulos.validate as v
import modulos.infoUsuario as i2
import modulos.Productos as pr
import modulos.compañia as com
import sys

Productos={}
core.checkFile('Ejercicio3.json',Productos)

compañia={
    'employes':{},
    'pays':{}
}
core.checkFile('Ejercicio4.json',compañia)


def Principal():

    titulo=''' 

        ++++++++++++++++++++++++++++++++++
        + Bienvenidos al menu del exmaen +
        ++++++++++++++++++++++++++++++++++
    
    '''
    menu=[['1. Conversion de moneda'],['2. Leer informacion del usuario'],['3. Registrar Productos de tienda'],['4. Registrar informacion de compañia'],['5. Salir']]
    
    isOpction=True

    while isOpction:
        op=v.opciones('Ingrese una opcion',titulo,tabulate(menu,tablefmt='fancy_grid'))
        
        if op==1:
            c.ConversioMoneda()
        elif op==2:
            i2.addUser()
        elif op==3:
            pr.Productos()
        elif op==4:
            menuEmpleados()
        elif op==5:
            sys.exit('Hasta luego')







def menuEmpleados():

    titulo=''' 

        +++++++++++++++++++++++++++++++++++
        + Bienvenidos al menu de empleaos +
        +++++++++++++++++++++++++++++++++++
    
    '''
    menu=[['1. Añadir Empleados'],['2. Añadir Pagos'],['3. Ver colilla de pago'],['4. Salir']]
    
    isOpction=True

    while isOpction:
        op=v.opciones('Ingrese una opcion',titulo,tabulate(menu,tablefmt='fancy_grid'))
        
        if op==1:
            com.addEmployess()
        elif op==2:
            com.addpay()
        elif op==3:
            com.seePays()
        elif op==4:
            isOpction=False
            core.pauseScreen()

    