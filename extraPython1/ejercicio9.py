def generar_n_caracteres(num, letra):
    cadena=""
    for i in range(num):
        cadena+=letra
    
    return cadena

print(generar_n_caracteres(6, 'r'))