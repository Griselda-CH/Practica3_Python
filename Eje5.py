"""5.- Desarrolla una función que sume los dígitos de un número de manera recursiva hasta obtener 
un solo dígito.
Dado un número entero positivo, suma sus dígitos repetidamente hasta que el resultado sea un solo dígito.
Por ejemplo, para el número 9876, sumamos 9 + 8 + 7 + 6 = 30, luego sumamos 3 + 0 = 3.
Escribe una función recursiva que tome un número entero positivo y devuelva el resultado de esta suma repetida.
La función debe manejar correctamente números de varias cifras y realizar las llamadas recursivas necesarias."""

def suma_digitos_enteros(n):
    if n < 10:       #si n es solo un digito lo retorna
        return n
    suma = 0
    while n > 0:
        suma += n% 10 #sumara el ultimo digito
        n //= 10      #esta accion eliminara el ultimo digito
    
    return suma_digitos_enteros(suma)
# El usuario podra ingresar un numero entero
numero = int(input("Ingresa un numero entero: "))

resultado = suma_digitos_enteros(numero)
print(f"La suma de los digitos de {numero} hasta el ultimo digito es: {resultado}") 
