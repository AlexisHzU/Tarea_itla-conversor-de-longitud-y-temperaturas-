import time
#formulas
#Fahrenheit a celsius (F -32) x 5/9
#Fahrenheit a kelvin (F - 32) x 5/9 + 273.15

def fahrenheit_celsius(fahre):
    return round((fahre - 32) * 5/9,2)

def fahrenheit_kelvin(fahre):
    return round((fahre - 32) * 5/9 + 273.15,2)

def eleccion():
    while True:
        elegir2 = int(input('''A que grado se llevara los Fahrenheit: 
1- Celsius
2- Kelvin
0- Salir
    '''))
        if elegir2 == 1:
            grados = float(input('Cuantos grados Fahrenheit son: '))
            print(f'Fahrenheit: {grados}° \nCelsius: {fahrenheit_celsius(grados)}°')
            time.sleep(1)
        elif elegir2 == 2:
            grados = float(input('Cuantos grados Fahrenheit son: '))
            print(f'Fahrenheit: {grados}° \nKelvin: {fahrenheit_kelvin(grados)}°')
            time.sleep(1)
        elif elegir2 == 0:
            break