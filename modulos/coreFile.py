import os 
import json

BASE='data/'

def clearScreen():
    if os.sys.platform=='linux' or os.sys.platform=='darwin':
        os.system('clear')
    else:
        os.system('cls')

def pauseScreen():
    input('Ingrese cualqier letra para continuar')


def checkFile(*params):
    if (os.path.isfile(BASE+params[0])):
        params[1].update(readFile(params[0]))
    else:
        createFile(params[0],params[1])


def readFile(*params)->dict:
    with open(BASE+params[0], 'r') as br:
        return json.load(br)

def createFile(*params):
    with open(BASE+params[0], 'w') as bw:
        json.dump(params[1],bw,indent=4)

def updateFile(*params):
    with open(BASE+params[0], 'w+') as bw:
        bw.seek(0)
        json.dump(params[1],bw,indent=4)