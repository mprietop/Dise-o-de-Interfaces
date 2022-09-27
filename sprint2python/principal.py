from fibonacci import funcion_fibonacci as fibonacci
from fibonacci2 import funcion_fibonacci as fibonacci2
import time

n = int(input("Introduzca el número: "))
op = input("Que método prefiere utilizar? a) b)")

while (op != 'a') & (op != 'b'):
    op = input("Que método prefiere utilizar? a) b)")
    
if op == 'a':
    start_time = time.time()
    print(fibonacci(n))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('El tiempo de ejecución ha sido :' + str(elapsed_time) + ' s')
    
else:
    start_time = time.time()
    print(fibonacci2(n))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('El tiempo de ejecución ha sido :' + str(elapsed_time) + ' s')