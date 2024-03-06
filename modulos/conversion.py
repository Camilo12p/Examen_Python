import modulos.validate as v
from tabulate import tabulate
import modulos.coreFile as core

def ConversioMoneda():
    #TITULOS A IMPRIMIR EN PANTALLA
    titulo=''' 

        ++++++++++++++++++++++++++++++++++++++++++
        + Bienvenidos a la conversion de monedas +
        ++++++++++++++++++++++++++++++++++++++++++
    
    '''

    titulo2='¿Que desea convertir?'
    menu=[['1. Peso a Dolares'],['2. Dolares a Pesos'],['3. Pesos a Euros'],['4. Euros a Pesos'],['5. Pesos a Yenes'],['6. Yenes a Pesos'],['7. Salir']]
    
    

    #SE HACE LA ELECCION DEL TIPO DE CONVERSION
    isOpction=True
    while isOpction:
        op=v.opciones('Ingrese una opcion',titulo,titulo2,tabulate(menu,tablefmt='fancy_grid')) #FUNCION QUE VERIFICA LA OPCION CORRECTA
        
        if op==1:
            conversion('Pesos','Dolares',1/3944)
        elif op==2:
            conversion('Dolares','Pesos',3944)
        elif op==3:
            conversion('Pesos','Euros',1/4279)
        elif op==4:
            conversion('Euros','Pesos',4279)
        elif op==5:
            conversion('Pesos','Yenes',1/26.30)
        elif op==6:
            conversion('Yenes','Pesos',26.30)
        elif op==7:
            isOpction=False
            core.pauseScreen()

def conversion(Moneda1:str,Moneda2,Pconversion:float):  #Funcion que hace la conversio, Moneda1/2 es el nombre de la moneda, Pconversion es la relacion de la conversion
    # SE PIDE EL CUANTA MONEDA VA A CONVERTIR
    A=v.flotantes(f'Ingrese la cantidad en {Moneda1}')
    # SE HACE LA CONVERSION  
    B = A*Pconversion
    # SE IMPRIME LA CONVERSION
    print(f'La conversion de {Moneda1} a {Moneda2} es: {B}')
    core.pauseScreen()

