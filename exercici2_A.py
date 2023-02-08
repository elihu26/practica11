def nombres5():
    """
    En este ejercicio, lo que he echo es crear una lista y poner 5 nombres,
    luego he creado un input que pone que inserte un nombre de los propuestos en
    la lista, dependiendo de el que ponga saldra un texto diferente pero si el nombre
    no se encuentra en la lista entonces saldra que no esta en la lista
    :return:
    """
    myList = ['David', 'Raul', 'Alex', 'Pablo', 'Miguel']
    nombres = (input("inserta un nombre de los 5 propuestos: David, Raul,Alex,Pablo,Miguel: "))
    if (nombres == "David"):
        print("Te llamas {myList}".format(myList="David"))
    elif (nombres == "Raul"):
        print("Te llamas {myList}".format(myList="Raul"))
    elif (nombres == "Alex"):
        print("Te llamas {myList}".format(myList="Alex"))
    elif (nombres == "Pablo"):
        print("Te llamas {myList}".format(myList="Pablo"))
    elif (nombres == "Miguel"):
        print("Te llamas {myList}".format(myList="Miguel"))
    else:
        print("Este nombre no esta en la lista")
    nombres5()
