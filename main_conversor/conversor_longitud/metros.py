import time
#formulas Metros
#Kilometro = Metro * 1000
#Millas =  Metros / 1609
#Pies = metros * 3.281

def metros_kilometros(metros):
    return metros / 1000

def metros_millas(metros):
    return metros / 1609

def metros_pies(metros):
    return round(metros * 3.281,2)

def eleccion():
    while True:
        elegir2 = int(input('''A que longitud se llevara los metros: 
1- Kilometros
2- Millas
3- Pies
0- Salir
    '''))
        if elegir2 == 1:
            long = float(input('Cuantos metros son: '))
            print(f'Metros: {long} \nKilometros: {metros_kilometros(long)}')
            time.sleep(1)
        elif elegir2 == 2:
            long = float(input('Cuantos metros son: '))
            print(f'Metros: {long} \nMillas: {metros_millas(long)}')
            time.sleep(1)
        elif elegir2 == 3:
            long = float(input('Cuantos metros son: '))
            print(f'Metros: {long} \nPies: {metros_pies(long)}')
            time.sleep(1)
        elif elegir2 == 0:
            break
