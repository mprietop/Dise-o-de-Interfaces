puntuacion = 0
def validacion(puntuacion,correcta):
    op = input("Tu respuesta: ")
    while (op != 'a') & (op != 'b') & (op != 'c'):
        op = input("Tu respuesta (a, b, c): ")

    if (op == correcta):
        print("Respuesta correcta +10 pts")
        puntuacion+=10
    else:
        print("Respuesta incorrecta -5 pts") 
        puntuacion-=5
    return puntuacion
        
print ("¿Cuántos jugadores hay en un campo de fútbol?")
print ("a) 24")
print ("b) 18")
print ("c) 22")
puntuacion = validacion(puntuacion,'c')


print ("¿Cuál es el planeta más cercano al Sol?")
print ("a) Venus")
print ("b) Mercurio")
print ("c) Tierra")
puntuacion = validacion(puntuacion,'b')

print ("¿Quién es el fundador de Apple?")
print ("a) Steve Jobs")
print ("b) Bill Gates")
print ("c) Hideo kojima")

print(str(validacion(puntuacion,'a')))



 