"""7.- EJERCICIO LIBRE:
HAZ UN SOFTWARE TOTALMENTE LIBRE QUE RESUELVA UN PROBLEMA EN ESPECÍFICO
¿QUÉ DEBEN USAR?
TODO LO QUE SE VIO EN CLASE HASTA EL TEMA DE POO (CLASES) NO SE ACEPTARÁ HERENCIA"""

#Esta aplicacion tiene como fin agregar estudiantes con sus respectivas notas en cada materia

#El Menu para poder interactuar con la aplicacion

def mostrar_menu():
    print ("\n--- Menu de Registro de Estudiantes")
    print ("1. Agregar Estudiante")
    print ("2. Mostrar Estudiante")
    print ("3. Eliminar Estudiante")
    print ("4. Cargar Datos")
    print ("5. Guardar datos")
    print ("6. Salir")

def main():
    registro = RegistroDeNotas()
    
    while true:
        mostrar_menu
        opcion = input("Selecione una opcion (1-6): ")
        
        if opcion == '1':
            agregar_estudiantes_interactivo(registro)
        elif opcion == '2':
            registro.mostrar_estudiantes()
        elif opcion == '3':   
            id_estudiante = input("Ingrese el Id del estudiante a eliminar: ")
            try: 
                registro.eliminar_estudiante(id_estudiante)
            except KeyError as e:
                print(e)
        elif opcion == '4':
            archivo = input("Ingrese el nombre del archivo para cargar datos (por ejemplo, estudiante.json): ")
            try:
                registro.cargar_datos(archivo)
                print("Datos cargados con exito.")
            except FileNotFoundError:
                print("Error: El archivo no se encontro:")
        elif opcion == '5':
            archivo = input("Ingrese el nombre del archivo para guardar datos (por ejemplo, estudiante,json): ")
            registro.guardar_datos(archivo)
            print("Datos guardados con exito.")
        elif opcion == '6':
            print("saliendo del programa")
            break
        else:
            print("Opcion no valida, por favor selecione una opcion del 1 al 6.")
if __name__ == "_main_":
    main()               
class Estudiante:
    def __init__(self, nombre, id_estudiante):
        self.nombre = nombre
        self.id_estudiante = id_estudiante
        self.notas = {}  # Diccionario para almacenar las materias y sus respectivas notas

    def agregar_nota(self, materia, nota):
        if 0 <= nota <= 100:  # Validacion de nota
            self.notas[materia] = nota
        else:
            raise ValueError("La nota debe estar entre 0 y 100.")

    def actualizar_nota(self, materia, nueva_nota):
        if materia in self.notas:
            if 0 <= nueva_nota <= 100:
                self.notas[materia] = nueva_nota
            else:
                raise ValueError("La nota debe estar entre 0 y 100.")
        else:
            raise KeyError(f"La materia {materia} no esta registrada para el estudiante {self.nombre}.")

    def actualizar_varias_notas(self, nuevas_notas):
        """Actualiza o agrega varias notas de una sola vez."""
        for materia, nota in nuevas_notas.items():
            self.agregar_nota(materia, nota)

    def calcular_promedio(self):
        if self.notas:
            total = sum(self.notas.values())
            promedio = total / len(self.notas)
            return promedio
        return 0

    def __str__(self):
        return f"Estudiante: {self.nombre}, ID: {self.id_estudiante}, Notas: {self.notas}"

class RegistroDeNotas:
    def __init__(self):
        self.estudiantes = {}  # Diccionario para almacenar estudiantes con su ID como clave

    def agregar_estudiante(self, nombre, id_estudiante, notas=None):
        """Agrega un estudiante al registro, con la opcion de agregar notas iniciales."""
        if id_estudiante not in self.estudiantes:
            estudiante = Estudiante(nombre, id_estudiante)
            self.estudiantes[id_estudiante] = estudiante
            if notas:  # Si se proporcionan notas, agregarlas
                estudiante.actualizar_varias_notas(notas)
            print(f"Estudiante {nombre} agregado con éxito.")
        else:
            raise ValueError(f"El estudiante con ID {id_estudiante} ya esta registrado.")

    def eliminar_estudiante(self, id_estudiante):
        if id_estudiante in self.estudiantes:
            del self.estudiantes[id_estudiante]
            print(f"Estudiante con ID {id_estudiante} eliminado.")
        else:
            raise KeyError(f"No existe un estudiante con ID {id_estudiante}.")

    def obtener_estudiante(self, id_estudiante):
        if id_estudiante in self.estudiantes:
            return self.estudiantes[id_estudiante]
        raise KeyError(f"No se encontro ningún estudiante con ID {id_estudiante}.")

    def mostrar_estudiantes(self):
        if self.estudiantes:
            for id_estudiante, estudiante in self.estudiantes.items():
                print(estudiante)
        else:
            print("No hay estudiantes registrados.")

# Funcion para interactuar con el usuario y agregar estudiantes y notas
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

                # Validacion de la nota dentro del rango 0-100
                while True:
                    try:
                        nota = float(input(f"Ingrese la nota para {materia} (0-100): "))
                        if 0 <= nota <= 100:
                            break  # Salir del bucle si la nota es válida
                        else:
                            print("Error: La nota debe estar entre 0 y 100.")
                    except ValueError:
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

# Uso del sistema de registro de notas con interacción
registro = RegistroDeNotas()

# Llamada para permitir al usuario agregar estudiantes y sus notas
agregar_estudiantes_interactivo(registro)

# Mostrar todos los estudiantes registrados
registro.mostrar_estudiantes()
