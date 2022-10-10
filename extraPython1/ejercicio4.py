vocales = ['a', 'e', 'i', 'o', 'u']

def esVocal(letra):
    if letra in vocales:
        return True
    else:
        return False
    
print(esVocal('v'))