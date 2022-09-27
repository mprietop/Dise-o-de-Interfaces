from fibonacci import funcion_fibonacci as fibonacci
from fibonacci2 import funcion_fibonacci as fibonacci2


n = int(input("Introduzca el número: "))
op = input("Que método prefiere utilizar? a) b)")

while (op != 'a') & (op != 'b'):
    op = input("Que método prefiere utilizar? a) b)")
    
if op == 'a':
    print(fibonacci(n))
else:
    print(fibonacci2(n))