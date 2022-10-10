def suma(lista):
    n = 0
    for i in lista:
        n+=i
        
    return n
    
def mult(lista):
    n = 1
    for i in lista:
        n*=i
    
    return n
        
  
print(suma([3, 5, 7]))
print(mult([2, 3, 5]))