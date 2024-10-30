import time
#formula
#kelvin a celsius = K - 273.14
#kelvin a fahrenheit = (K - 273.15) x 9/5 + 32

def kelvin_celsius(kelvin):
    return round(kelvin - 273.15,2)

def kelvin_fahrenheit(kelvin):
    return round((kelvin - 273.15) * 9/5 + 32,2)

def eleccion():
    while True:
        elegir2 = int(input('''A que grado se llevara los Kelvin: 
1- Celsius
2- Fahrenheit
0-Salir
    '''))
        if elegir2 == 1:
            grados = float(input('Cuantos grados Kelvin son: '))
            print(f'Kelvin: {grados}° \nCelsius: {kelvin_celsius(grados)}°')
            time.sleep(1)
        elif elegir2 == 2:
            grados = float(input('Cuantos grados Kelvin son: '))
            print(f'Kelvin: {grados}° \nFahrenheit: {kelvin_fahrenheit(grados)}°')
            time.sleep(1)
        elif elegir2 == 0:
            break

