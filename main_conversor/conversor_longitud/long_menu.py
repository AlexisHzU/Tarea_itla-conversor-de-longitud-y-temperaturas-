from conversor_longitud import metros,kilometros,millas,pies

def main():
    while True:
        print('''
Bienvenido a la calculadora de longitudes
Que longitud desea calcular:
1-Metros
2-Kilometros
3-Millas
4-Pies
0- Salir''')
        elegir = int(input())
        print('----------------------------')
        if elegir == 1:
            metros.eleccion()
        elif elegir == 2:
            kilometros.eleccion()
        elif elegir == 3:
            millas.eleccion()
        elif elegir == 4:
            pies.eleccion()
        else:
            break
        print('----------------------------')