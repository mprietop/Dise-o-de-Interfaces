def superposicion(cadena1, cadena2):
    superpuestos = False
    for i in range(len(cadena1)):
        if cadena1[i]==cadena2[i]:
            superpuestos = True
            
    return superpuestos

print(superposicion('casa', 'aaul'))