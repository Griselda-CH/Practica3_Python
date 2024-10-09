""""2.- Desarrolla una función en Python que invierta una cadena de texto sin utilizar el operador de slicing.
El objetivo de este ejercicio es escribir una función que tome una cadena de caracteres y la devuelva invertida, 
pero sin hacer uso del operador de slicing ([::-1]). 
La función debe recorrer cada carácter de la cadena de entrada y construir una nueva cadena con los
caracteres en orden inverso. Por ejemplo, si la función recibe "python", debe retornar "nohtyp". 
Asegúrate de no usar atajos como métodos incorporados que realicen la inversión por ti."""

"""funcion len() se usa para obtener el número de dígitos que lo componen.
(del número de elementos) de un objeto.""" 

texto=input("Introduce la cadena: ")
def invertir_cadena(cad):
    nueva_cad = ""
    
    ##Esto permite acceder a los caracteres en orden inverso.
    for i in range(len(cad) - 1, -1, -1):
    ##Añade cada carácter en orden inverso a nueva_cadena
        nueva_cad += cad[i]
    
    return nueva_cad

resultado = invertir_cadena(texto)
print(resultado)