def inversa(cadena):
    invertida=''
    for i in reversed(cadena):
        invertida+=i
    
    return invertida


print(inversa('Mario'))