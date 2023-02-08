""""En aquest arxiu s’hi crearà una funció on demanarà a
 l’usuari que inserti 2 números i el programa li dirà quin és el més gran
  i quin el més petit. Si son iguals, no sortirà cap missatge."""
def exercici1B():
  x = int(input("Indica cual es el primer numero : "))
  y = int(input("Indica el segundo numero: "))
  #indico los inputs para que el usuario ponga los numeros que quiera.
  if x > y:
    print('El número mas grande es {x} y el mas pequeño es {y}'.format(x=x, y=y))
  elif x < y:
    print('El número mas grande es {y} y el mas pequeño es {x}'.format(y=y, x=x))
  else:
    print('Es el mismo número.')

#La primera condicion, si el primer numero es mas grande que el segundo , se indicara por pantalla usando el comando format en el print.
# En caso contrario se pondra que es el segundo numero el mas grande y en caso de ser iguales tambien se indicara por pantalla.