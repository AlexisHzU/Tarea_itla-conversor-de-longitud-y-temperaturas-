import time
#formulas Pies
#pies a metros = pie / 3.281
#pies a kilometros = pie / 3281
#pies a millas = pie / 5280

def pies_metros(pies):
    return pies / 3.281

def pies_kilometros(pies):
    return pies / 3281

def pies_millas(pies):
    return pies / 5280

def eleccion():
    while True:
        elegir2 = int(input('''A que longitud se llevara los Pies: 
1- Metros
2- Kilometros
3- Millas
0- Salir
    '''))
        if elegir2 == 1:
            long = float(input('Cuantos Pies son: '))
            print(f'Pies: {long} \nMetros: {pies_metros(long)}')
            time.sleep(1)
        elif elegir2 == 2:
            long = float(input('Cuantos Pies son: '))
            print(f'Pies: {long} \nKilometros: {pies_kilometros(long)}')
            time.sleep(1)
        elif elegir2 == 3:
            long = float(input('Cuantos Pies son: '))
            print(f'Pies: {long} \nMillas: {pies_millas(long)}')
            time.sleep(1)
        elif elegir2 == 0:
            break


