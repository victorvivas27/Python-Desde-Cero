from os import system

# ----------------------------------------------------------
# LIMPIAR LA CONSOLA (OPCIONAL)
# ----------------------------------------------------------
# Intentamos limpiar la consola según el sistema operativo:
# - "clear" → Linux / macOS
# - "cls"   → Windows
# Si el primer comando falla, se ejecuta el segundo
if system("clear") != 0:
    system("cls")


# ==========================================================
# CLASES EN PYTHON
# ==========================================================
# Una clase es una plantilla que permite crear objetos.
# Un objeto es una instancia de una clase.
#
# Las clases permiten:
# - Agrupar datos (atributos / propiedades)
# - Agrupar comportamientos (métodos)
#
# Esto es la base de la Programación Orientada a Objetos (POO).
# ==========================================================


# ----------------------------------------------------------
# DEFINICIÓN DE LA CLASE
# ----------------------------------------------------------
# Convenciones:
# - Nombre de la clase → Singular y CamelCase
# - Atributos → minúsculas y snake_case
class Coche:

    # ------------------------------------------------------
    # ATRIBUTOS DE CLASE
    # ------------------------------------------------------
    # Son compartidos por TODAS las instancias de la clase
    ruedas = 4
    tipo = "Vehículo de cuatro ruedas"

    # ------------------------------------------------------
    # MÉTODO ESPECIAL __init__
    # ------------------------------------------------------
    # Se ejecuta automáticamente cuando se crea un objeto
    #
    # self:
    # - Hace referencia al objeto que se está creando
    # - Permite acceder a atributos y métodos del objeto
    def __init__(self, marca, modelo):

        # Atributos de instancia
        # Cada objeto tiene sus propios valores
        self.marca = marca
        self.modelo = modelo

    # ------------------------------------------------------
    # MÉTODO DE INSTANCIA
    # ------------------------------------------------------
    # Define un comportamiento del objeto
    def arrancar(self):
        print(f"El coche {self.marca} {self.modelo} arrancó correctamente")


# ==========================================================
# CREACIÓN DE OBJETOS (INSTANCIAS)
# ==========================================================

# Creamos un objeto de la clase Coche
toyota = Coche("Toyota", "Corolla")

# Llamamos a un método del objeto
toyota.arrancar()

# Creamos otro objeto de la misma clase
ford = Coche("Ford", "Fiesta")

# Cada objeto tiene sus propios datos
ford.arrancar()


# ==========================================================
# CONCEPTOS CLAVE APLICADOS
# ==========================================================
# ✔ Clase: Coche
# ✔ Objeto: toyota, ford
# ✔ Atributos de clase: ruedas, tipo
# ✔ Atributos de instancia: marca, modelo
# ✔ Método: arrancar()
# ✔ Encapsulamiento:
#   - No importa cómo funciona arrancar()
#   - Solo se llama al método y se ejecuta
