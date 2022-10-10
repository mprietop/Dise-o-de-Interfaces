def longitud(palabra):
    if isinstance(palabra, list) or isinstance(palabra, str):
        n=0
        for i in palabra:
            n+=1
        return n
        
        
lista = 'uyui'

print(longitud(lista))