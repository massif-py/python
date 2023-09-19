from colorama import init, Fore, Back

init(autoreset=True)
print(Back.GREEN + 'UNIVERSIDAD UTEL')
print(Back.GREEN + 'Sistema de promedios de calificaciones')

c = []
option = 's'
while(option == 's' or option == 'S'):
    calification = float(input(Back.CYAN + 'Ingresa la calificación:' + Back.RESET))
    c.append(calification)
    option = input(Back.RED + '¿Desea introducir otra calificación? [s/S][n/N]:' + Back.RESET)
print(Back.YELLOW + 'El promedio de calificaciones es:', round(sum(c)/len(c), 2))

#(GAVRIEL ANAYA DELGADO).py
        
