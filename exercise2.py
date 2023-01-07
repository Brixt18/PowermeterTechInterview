#  Partiendo del siguiente código y utilizando la menor cantidad de líneas, resuelva los siguientes puntos:

# CODE
import json

repetidos = [1,2,3,"1","2","3",3,4,5]

r = [1,"5",2,"3"]

d_str = '{"valor":125.3,"codigo":123}'

# ANSWER
# 1. Genere una lista con los valores no repetidos de la lista ‘repetidos’.
# 2. Genere una lista con los valores en común entre la lista ‘r’ y ‘repetidos’
# 3. Transforme ‘d_str’ en un diccionario.

def _convert_to_same_type(lista:list):
    # Esta variable convierte la lista a una lista con todos los objetos del mismo tipo, str en este caso.
    # Esto es para comparar todos de la misma manera y así no generar redundancia, ya que talvez tanto 1 (int) como "1" (str)
    # hagan referencia a la misma cosa...    
    return list(map(lambda x: str(x), lista))

def ex1(lista:list, same_type:bool=False):
    if same_type:
        lista = _convert_to_same_type(lista)

    return [x for x in lista if not lista.count(x) > 1]

def ex2(lista1:list, lista2:list, same_type:bool=False):
    if same_type:
        lista = _convert_to_same_type(lista)

    return list(filter(lambda x: x in lista1, lista2))

def ex3(lista:str):
    return json.loads(lista)

if __name__ == "__main__":
    print(ex1(repetidos))
    print(ex2(repetidos, r))
    print(ex3(d_str), type(ex3(d_str)))
