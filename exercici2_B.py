#En aquest arxiu s’hi crearà una funció on demanarà a l’usuari que indiqui un número i aquest li indicarà si és parell o senar.
x = int(input('Indica un numero i et dire si es parell o senar: '))
def exercici2B():
    if x % 2 == 0:
        print('{x} es parell'.format(x=x))
    else:
        print('{x} es senar'.format(x=x))

#con el x % 2 puedo saber si es parejo si el resultado es 0 , primera condicion si es par y el else si es inpar.