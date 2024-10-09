"""3.- Escribe una función que calcule el factorial de un número entero de forma iterativa.
El factorial de un número n (denotado como n!) es el producto de todos los números enteros 
positivos desde 1 hasta n. Por ejemplo, el factorial de 5 es 5! = 5 × 4 × 3 × 2 × 1 = 120.
Escribe una función que reciba un número entero positivo y devuelva su factorial.
Debes implementar la función usando un bucle for, multiplicando el valor de cada número
por el resultado acumulado. Además, considera casos en los que el número sea 0 o negativo."""

numero= int(input('Introduce un número: '))

def factorial(n):
    if n < 0:
        return "El número debe ser un entero positivo."
    # El factorial de 0 y 1 es 1
    elif n == 0 or n == 1:
        return 1
    
    resultado = 1
    
 ##genera una secuencia de números desde 2 incluyendo n
    for i in range(2, n + 1):
            resultado *= i
    return resultado

resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}.")