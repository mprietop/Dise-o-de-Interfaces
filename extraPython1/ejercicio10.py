def histograma(lista):
    for i in lista:
        cadena=""
        for j in range(len(i)):
            cadena+='*'
        print(cadena)
            
histograma(["casa", "las casas", "el niño"])