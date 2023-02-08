def numeroGran():
    """En este ejercicio nos pide que ingresemos 2 numeros y que luego si el primer numero
    es mas grande saldra por pantalla el primer mensaje, si el 2 numero es mas grande saldra
    por pantalla el segundo, y si son iguales saldra por pantalla que los 2 son iguales
    """
    x = int(input("Cual es el primer numero?"))
    y = int(input("Cual es el segundo numero?"))
    if (x > y):
        print("el numero {x} es mas grande que el {y}".format(x=x, y=y))
    elif (y > x):
        print("el numero {y} es mas grande que el {x}".format(y=y, x=x))
    else:
        print("son iguales")
    numeroGran()