print ("¿Cuántos jugadores hay en un campo de fútbol?")
print ("a) 24")
print ("b) 18")
print ("c) 22")
op = input("Tu respuesta: ")

while (op != 'a') & (op != 'b') & (op != 'c'):
    op = input("Tu respuesta (a, b, c): ")

if (op == 'c'):
    print("Respuesta correcta")
else:
    print("Respuesta incorrecta") 