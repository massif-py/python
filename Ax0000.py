from colorama import Back

edades = []
counter = 0
while 1:
    counter += 1
    edad = input(Back.BLUE + 
                 f'Ingresa la edad {counter}:' +
                 Back.RESET)
    try:
        edades.append(int(edad))
    except ValueError:
        print(Back.RED + 
              'Ingresa una edad que sea valida.' +
              Back.RESET)
        counter -= 1
    if counter == 10:
        break
print(Back.YELLOW + 'El promedio de la edades es' + Back.RESET, sum(edades)/len(edades))