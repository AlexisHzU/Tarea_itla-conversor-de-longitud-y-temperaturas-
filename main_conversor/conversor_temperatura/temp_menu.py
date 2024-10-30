from conversor_temperatura import celsius,fahrenheit,kelvin


def main():
    while True:
        print('''
Bienvenido a la calculadora de temperaturas
Que grado desea calcular:
1-Celsius
2-Fahrenheit
3-Kelvin
0- Salir''')
        elegir = int(input())
        print('----------------------------')
        if elegir == 1:
            celsius.eleccion()
        elif elegir == 2:
            fahrenheit.eleccion()
        elif elegir == 3:
            kelvin.eleccion()
        else:
            break
        print('----------------------------')



