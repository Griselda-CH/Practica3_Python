"""4. Crea una función que determine si una palabra o frase es un palíndromo, ignorando mayúsculas y espacios.
Un palíndromo es una palabra o frase que se lee igual de adelante hacia atrás y de atrás hacia adelante, 
ignorando espacios y mayúsculas. Por ejemplo, "Anita lava la tina" es un palíndromo. 
Escribe una función que reciba una cadena de caracteres y determine si es un palíndromo. 
La función debe ser capaz de ignorar los espacios y no diferenciar entre letras mayúsculas y minúsculas. 
Debes recorrer la cadena y comparar sus caracteres de manera inversa sin usar el método de slicing ([::-1])."""

texto=input("Introduce una cadena: ")

def es_palindromo(cadena):
    # Limpiar la cadena: divide la cadena en una lista de palabras,
    # eliminar espacios y convertir a minúsculas
    cadena_limpia = ''.join(cadena.split()).lower()
    
    # Comparar la cadena limpia con su reverso
    return cadena_limpia == cadena_limpia[::-1]

if es_palindromo(texto):
    print(f'"{texto}" es un palíndromo.')
else:
    print(f'"{texto}" no es un palíndromo.')