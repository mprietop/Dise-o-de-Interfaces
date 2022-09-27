print ("¿Cuántos jugadores hay en un campo de fútbol?")
print ("a) 24")
print ("b) 18")
print ("c) 22")
op = input("Tu respuesta: ")
correcta = 'c'

validacion_repuesta(correcta, op)

def validacion_repuesta(cor, op):
    while (o != 'a') & (o != 'b') & (o != 'c'):
        o = input("Tu respuesta (a, b, c): ")
        
    if (o == correcta):
        print("Respuesta correcta")
    else:
        print("Respuesta incorrecta") 