

def funcion_fibonacci(n):
    
    if n == 0:
      enesimo = 0
    elif n == 1:
        enesimo = 1
    elif n > 1:
        enesimo = funcion_fibonacci(n-1) + funcion_fibonacci(n-2)
    
    return enesimo 