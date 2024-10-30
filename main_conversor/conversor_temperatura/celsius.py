import time 
#Formula de Celsius a fahrenheit
#Grados Fahrenheit = (grados centígrados × 9/5) +32.
#Grados kelvin = centigrados + 273.15

def Celsius_Fahrenheit(celsius):
    return round((celsius * 9 / 5) + 32,2)

def Celsius_Kelvin(celsius):
    return round(celsius + 273.15,2)

def eleccion():
    while True:
        elegir2 = int(input('''A que grado se llevara los Celsius: 
1- Fahrenheit
2- Kelvin
0- Salir
    '''))
        if elegir2 == 1:
            grados = float(input('Cuantos grados celsius son: '))
            print(f'Celsius: {grados}° \nFahrenheit: {Celsius_Fahrenheit(grados)}°')
            time.sleep(1)
        elif elegir2 == 2:
            grados = float(input('Cuantos grados celisus son: '))
            print(f'Celsius: {grados}° \nKelvin: {Celsius_Kelvin(grados)}°')
            time.sleep(1)
        elif elegir2 == 0:
            break

