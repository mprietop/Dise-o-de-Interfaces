from ejercicio6 import inversa

def esPalindromo(cadena):
   
    if cadena.lower() == inversa(cadena.lower()):
        return True
    else:
        return False
    
print(esPalindromo('Anna'))