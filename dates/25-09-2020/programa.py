import re

def elimina_espacios(segmento):
    segmento2=re.sub(' +', ' ', segmento)
    return(segmento2)
    
    
    
fraseprueba="Este  es un ejemplo    con múltiples        espacios"
resultado=elimina_espacios(fraseprueba)
print(resultado)
