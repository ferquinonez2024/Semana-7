class Archivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.archivo = None
        print(f"Constructor: El archivo '{self.nombre}' ha sido creado.")

    def abrir_archivo(self, modo):
        self.archivo = open(self.nombre, modo)
        print(f"Archivo '{self.nombre}' abierto en modo '{modo}'.")

    def escribir_datos(self, datos):
        if self.archivo and not self.archivo.closed:
            self.archivo.write(datos)
            print(f"Datos escritos en el archivo '{self.nombre}'.")
        else:
            print(f"No se puede escribir en el archivo '{self.nombre}' porque no está abierto.")

    def __del__(self):
        if self.archivo:
            self.archivo.close()
            print(f"Destructor: El archivo '{self.nombre}' ha sido cerrado y el recurso limpiado.")

# Creación de instancias y demostración de funcionalidad
archivo = Archivo("mi_archivo.txt")  # Llama al constructor
archivo.abrir_archivo("w")  # Abre el archivo en modo escritura
archivo.escribir_datos("Este es un ejemplo de uso de constructores y destructores en Python.")  # Escribe datos

# Si no cerramos explícitamente el archivo, el destructor lo hará
# del archivo  # Opcional: llama explícitamente al destructor para limpiar recursos
