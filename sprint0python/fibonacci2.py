import math

def funcion_fibonacci(n):
    a = (1+math.sqrt(5))/2
    b = (1-math.sqrt(5))/2
    
    return (a ** n - b ** n) // math.sqrt(5)