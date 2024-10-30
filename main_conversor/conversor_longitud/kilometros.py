import time
#formulas de kilometros
#kilometros a metros = k * 1000
#kilometros  a millas = k / 1.609
#kilometros a pies = k x 3281

def kilometro_metros(kilometro):
    return kilometro * 1000

def kilometro_millas(kilometro):
    return kilometro / 1.609

def kilometro_pies(kilometro):
    return kilometro * 3281

def eleccion():
    while True:
        elegir2 = int(input('''A que longitud se llevara los kilometros: 
1- Metros
2- Millas
3- Pies
0- Salir
'''))
        if elegir2 == 1:
            long = float(input('Cuantos kilometros son: '))
            print(f'Kilometros: {long} \nMetros: {kilometro_metros(long)}')
            time.sleep(1)
        elif elegir2 == 2:
            long = float(input('Cuantos kilometros son: '))
            print(f'Kilometros: {long} \nMillas: {kilometro_millas(long)}')
            time.sleep(1)
        elif elegir2 == 3:
            long = float(input('Cuantos kilometros son: '))
            print(f'Kilometros: {long} \nPies: {kilometro_pies(long)}')
            time.sleep(1)
        elif elegir2 == 0:
            break