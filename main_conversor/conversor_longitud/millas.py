import time
#formulas millas
#millas a metros = ml x 1609
#millas a kilometro = ml x  1.609
#millas a pie =  ml x 5280

def millas_metros(millas):
    return millas * 1609

def millas_kilometros(millas):
    return millas * 1.609

def millas_pie(millas):
    return millas * 5280

def eleccion():
    while True:
        elegir2 = int(input('''A que longitud se llevara las millas: 
1- Metros
2- Kilometros
3- Pies
0- Salir
    '''))
        if elegir2 == 1:
            long = float(input('Cuantas millas son: '))
            print(f'Millas: {long} \nMetros: {millas_metros(long)}')
            time.sleep(1)
        elif elegir2 == 2:
            long = float(input('Cuantas millas son: '))
            print(f'Millas: {long} \nKilometros: {millas_kilometros(long)}')
            time.sleep(1)
        elif elegir2 == 3:
            long = float(input('Cuantas millas son: '))
            print(f'Millas: {long} \nPies: {millas_pie(long)}')
            time.sleep(1)
        elif elegir2 == 0:
            break




