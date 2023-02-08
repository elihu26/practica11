"""En aquest arxiu s’hi crearà una funció on li demanarà a l’usuari
l’edat i els ingressos que té mensuals. Si la resposta de l’edat és ser
igual o major de 18 anys i els ingressos son majors de 1200, el missatge per consola serà
“És necessari que facis la declaració d’hisenda”.
En cas que alguna de les dues opcions no es compleixi, el missatge serà
“Encara no pots fer la declaració”.
"""
def exercici3B():
    edad = int(input('Indica la teva edad: '))
    ingressos = int(input('Indica els teus ingressos mensuals: '))
#Los inputs para que el usuario indique su edad y sus ingresos y asi poder calcular si debe o no para a hacienda.
    if (edad >= 18) and (ingressos>1200):
        print('És necessari que facis la declaració d’hisenda')
    else:
    print('Encara no pots fer la declaració')
#Si alguna de esas 2 condiciones que se indican en el if no se cumple saltara el else y directamente saldra que aun no puede hacer declaracion.