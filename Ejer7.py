"""7.- EJERCICIO LIBRE:
HAZ UN SOFTWARE TOTALMENTE LIBRE QUE RESUELVA UN PROBLEMA EN ESPECÍFICO
¿QUÉ DEBEN USAR?
TODO LO QUE SE VIO EN CLASE HASTA EL TEMA DE POO (CLASES) NO SE ACEPTARÁ HERENCIA"""
#Esta aplicacion tiene como fin agregar estudiantes con sus respectivas notas en cada materia

class Estudiante:
    def __init__(self, nombre, id_estudiante):
        self.nombre = nombre
        self.id_estudiante = id_estudiante
        self.notas = {}  # Diccionario para almacenar las materias y sus respectivas notas

    def agregar_nota(self, materia, nota):
        if 0 <= nota <= 100:  # Validación de nota
            self.notas[materia] = nota
        else:
            raise ValueError("La nota debe estar entre 0 y 100.")

    def calcular_promedio(self):
        if self.notas:
            total = sum(self.notas.values())
            promedio = total / len(self.notas)
            return promedio
        return 0

    def actualizar_varias_notas(self, nuevas_notas):
        """Actualiza o agrega varias notas de una sola vez."""
        for materia, nota in nuevas_notas.items():
            self.agregar_nota(materia, nota)

    def __str__(self): # Este metodo define como se presentara el objeto como una cadena
        promedio = self.calcular_promedio()
        return f"Estudiante: {self.nombre}, ID: {self.id_estudiante}, Notas: {self.notas}, Promedio: {promedio:.2f}"

class RegistroDeNotas:
    def __init__(self):
        self.estudiantes = {}  # Diccionario para almacenar estudiantes con su ID como clave

    def agregar_estudiante(self, nombre, id_estudiante, notas=None):  #Agrega un estudiante nuevo al diccionario
        if id_estudiante not in self.estudiantes:  # Comprueba si el id del estudiante ya esta regsitrado
            estudiante = Estudiante(nombre, id_estudiante) # Si el ID es nuevo crea un objeto estudiante
            self.estudiantes[id_estudiante] = estudiante
            if notas:  # Si se proporcionan notas, agregarlas
                estudiante.actualizar_varias_notas(notas)
            print(f"Estudiante {nombre} agregado con éxito.")
        else:
            raise ValueError(f"El estudiante con ID {id_estudiante} ya está registrado.") # Si el ID ya existe lo exceptua Value Error

#Permite eliminar estudiantes del registro

    def eliminar_estudiante(self, id_estudiante):
        if id_estudiante in self.estudiantes:
            del self.estudiantes[id_estudiante]
            print(f"Estudiante con ID {id_estudiante} eliminado.")
        else:
            raise KeyError(f"No existe un estudiante con ID {id_estudiante}.")

    def mostrar_estudiantes(self):
        if self.estudiantes:
            for id_estudiante, estudiante in self.estudiantes.items():
                print(estudiante)
        else:
            print("No hay estudiantes registrados.")

    def mostrar_promedio_estudiante(self, id_estudiante):
        """Muestra el promedio de un estudiante específico."""
        if id_estudiante in self.estudiantes:
            estudiante = self.estudiantes[id_estudiante]
            promedio = estudiante.calcular_promedio()
            print(f"El promedio de {estudiante.nombre} es: {promedio:.2f}")
        else:
            print(f"No se encontró un estudiante con ID {id_estudiante}.")

# Función para interactuar con el usuario y agregar estudiantes y notas
# La funcion While True permite iniciar un bucle hasta que el usuario lo detenga
def agregar_estudiantes_interactivo(registro):
    while True:
        nombre = input("Ingrese el nombre del estudiante: ")
        id_estudiante = input("Ingrese el ID del estudiante: ")

        # Preguntar si se desean agregar notas
        agregar_notas = input("¿Desea agregar notas para este estudiante? (s/n): ").lower()
        notas = {}
        if agregar_notas == 's':
            while True:
                materia = input("Ingrese el nombre de la materia: ")

                # Validación de la nota dentro del rango 0-100
                while True:
                    try:     # El metodo Try permite manejar posibles excepciones durante la conversacion
                        nota = float(input(f"Ingrese la nota para {materia} (0-100): ")) # Nos permite interactuar con decimales
                        if 0 <= nota <= 100:
                            break  # Salir del bucle si la nota es válida
                        else:
                            print("Error: La nota debe estar entre 0 y 100.")
                    except ValueError: #Si la conversacion con FLoat falla se lanza una exepcion 
                        print("Error: Debe ingresar un valor numérico para la nota.")

                notas[materia] = nota

                continuar = input("¿Desea agregar otra materia? (s/n): ").lower()
                if continuar != 's':
                    break

        # Agregar el estudiante con las notas (si las hay)
        try:
            registro.agregar_estudiante(nombre, id_estudiante, notas)
        except ValueError as e:
            print(e)

        continuar = input("¿Desea agregar otro estudiante? (s/n): ").lower()
        if continuar != 's':
            break

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Menú de Registro de Estudiantes ---")
    print("1. Agregar Estudiante")
    print("2. Mostrar Estudiantes")
    print("3. Eliminar Estudiante")
    print("4. Mostrar Promedio de un Estudiante")
    print("5. Salir")

# Función principal para el menú interactivo
def main():
    registro = RegistroDeNotas()  # Crear un registro de notas vacío

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            agregar_estudiantes_interactivo(registro)
        elif opcion == '2':
            registro.mostrar_estudiantes()
        elif opcion == '3':
            id_estudiante = input("Ingrese el ID del estudiante a eliminar: ")            
            try:
                registro.eliminar_estudiante(id_estudiante)
            except KeyError as e: #Si el estudiante no se encuentra  se lanza una excepcion 
                print(e)
        elif opcion == '4':
            id_estudiante = input("Ingrese el ID del estudiante para mostrar su promedio: ")
            registro.mostrar_promedio_estudiante(id_estudiante)
        elif opcion == '5':
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida, por favor seleccione una opción del 1 al 5.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
