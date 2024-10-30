import conversor_temperatura.temp_menu as temp
import conversor_longitud.long_menu as long

while True:
    print('''
Bienvenido que calculo desea utilizar:
1- Calculos de Temperaturas
2- Calculos de Longitudes
0- Salir''')
    elegir = int(input())

    if elegir == 1:
        temp.main()
    elif elegir == 2:
        long.main()
    elif elegir == 0:
        print('gracias por utilizar mi servicio son 30000000000 dolares')
        exit()


