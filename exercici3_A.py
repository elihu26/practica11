def aleatorio():
    import random
    """en este ejercicio lo que tengo que hacer es crear 2 varibles: una con un numero random y otra 
    con un numero insertado por el usuario, luego tiene que adivinar si el numero que ha puesto es en el que estoy pensando
    """
    intentosRealizados = 0
    random = random.randrange(0, 100)
    estimacion = input()
    usuario = int(input("Ingrese un numero del 0 al 100: "))
    while (random < 6):
        print("Adivina")
        estimacion = int(estimacion)
        intentosRealizados = intentosRealizados + 1
        if estimacion < usuario:
            print('Tu estimación es muy baja.')

        elif estimacion > usuario:
            print('Tu estimación es muy alta.')

        else:
            estimacion == usuario
            break
    if estimacion == usuario:
        intentosRealizados = str(intentosRealizados)
        print("buen trabajo has adivinado mi numero en {intentosRealizados} intentos".format(intentosRealizados))
    aleatorio()










