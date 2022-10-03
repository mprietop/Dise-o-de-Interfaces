import random
puntuacion = 0
preguntasRespondidas = 0
numPregunta = 0
preguntas = [1, 2, 3]
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
        
       
while preguntasRespondidas < 2:
    print(preguntas)
    numPregunta = preguntas[random.choice(preguntas)] 
    if numPregunta == 1: 
        print ("¿Cuántos jugadores hay en un campo de fútbol?")
        print ("a) 24")
        print ("b) 18")
        print ("c) 22")
        puntuacion = validacion(puntuacion,'c')
        preguntas.remove(1)
        preguntasRespondidas+=1
    elif numPregunta == 2:
        print ("¿Cuál es el planeta más cercano al Sol?")
        print ("a) Venus")
        print ("b) Mercurio")
        print ("c) Tierra")
        puntuacion = validacion(puntuacion,'b')
        preguntas.remove(2)
        preguntasRespondidas+=1
    elif numPregunta == 3:
        print ("¿Quién es el fundador de Apple?")
        print ("a) Steve Jobs")
        print ("b) Bill Gates")
        print ("c) Hideo kojima")
        print(str(validacion(puntuacion,'a')))
        preguntas.remove(3)
        preguntasRespondidas+=1
        
        
print("Puntuación total: "+puntuacion)



 