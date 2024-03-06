import modulos.coreFile as core
import modulos.validate as v
from tabulate import tabulate


def addEmployess():
    # SE ACTUALIZA EL USUARIO PARA TENER LA INFORMACION MAS ACTUALIZADA
    data={}
    data.update(core.readFile('Ejercicio4.json'))
    # SE PIDE INFORMACION AL USUARIO
    id=v.newEmploye('Ejercicio4.json')
    nombre=v.cadenas('Ingrese el nombre completo del empleado')
    cargo=v.cargo()
    salario=v.flotantes('Ingrese el salario base mensual')
    # SE CREA UN DICCIONARIO
    employe={
        'id':id,
        'nombre':nombre,
        'cargo':cargo,
        'salario':salario
    }
    # SE ACTUALIZA EL SISTEMA LOCAL Y JSON
    data.get('employes').update({id:employe})
    core.updateFile('Ejercicio4.json',data)
    core.pauseScreen()


def addpay():
    # SE ACTUALIZA EL USUARIO PARA TENER LA INFORMACION MAS ACTUALIZADA
    data={}
    data.update(core.readFile('Ejercicio4.json'))
    
    HEXTRA=5500
    # SE PIDE INFORMACION AL USUARIO Y SE HACEN CALCULOS 
    id=v.Employe('Ejercicio4.json')
    valordia=float(data.get('employes').get(str(id)).get('salario'))/30
    diasTrabajados=v.diasTrabajados()
    horasExtras=v.flotantes('Ingrese las horas extras trabajados')
    descuentoxCafeteria=v.flotantes('Ingrese la cantidad dde descuento de cafeteria')
    cuotaPrestamos=v.flotantes('Ingrese la cantida de la cuota por prestamo')
    mesPagado=v.cadenas('Ingrese el mes pagado')
    fechaPago=input('Ingrese la fecha de pago dd/mm/yyyy')

    totalAPagar=(valordia*diasTrabajados) - descuentoxCafeteria - cuotaPrestamos + (horasExtras*HEXTRA)

    # SE CREA UN DICCIONARIO
    recibo={
        'mesPagado':mesPagado,
        'fechaPago':fechaPago,
        'sueldoBase':float(data.get('employes').get(str(id)).get('salario')),
        'valorTotalHrasExtras':horasExtras,
        'cuotaPrestamo':cuotaPrestamos,
        'descuentoxCafeteria':descuentoxCafeteria,
        'totalAPagar': totalAPagar
    }

    # SE ACTUALIZA EL SISTEMA LOCAL Y JSON PERO ANTES SE VALIDA SI YA HAY CREADO UN PAGO AL ID EN ESPECIFICO
    if str(id) in data.get('pays'):
        data.get('pays').get(str(id)).update({mesPagado:recibo})
    else:
        data.get('pays').update({id:{mesPagado:recibo}})
    core.updateFile('Ejercicio4.json',data)
    core.pauseScreen()

def seePays():
    # SE ACTUALIZA EL USUARIO PARA TENER LA INFORMACION MAS ACTUALIZADA
    data={}
    data.update(core.readFile('Ejercicio4.json'))
    pago=[]
    # SE PIDE INFORMACION AL USUARIO
    id=v.pays('Ejercicio4.json')
    # SE GUARDA LA INFORMACION EN UN ARRAY 
    for key,value in data.get('pays').get(str(id)).items():
        pago.append([value['mesPagado'],value['fechaPago'],value['sueldoBase'],value['valorTotalHrasExtras'],value['descuentoxCafeteria'],value['totalAPagar']])
    # SE CREA EL ENCABEZADO DE LA TABLA
    headers=['Mes pagado','Fecha de pago','Sueldo Base','Valoe de horas extras','descuentos de cafeteria','Total a pagar']
    # SE IMPRIME LA TABLA 
    print(tabulate(pago,headers=headers,tablefmt='fancy_grid'))
    core.pauseScreen()

