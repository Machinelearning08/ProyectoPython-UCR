import os

class ManipularArchivo:

    __archivo_cargado = None

    def cargar_archivo(self, ruta_del_archivo):
        self.__archivo_cargado = open(f"./archivos/{ruta_del_archivo}", 'a+')
        return "El archivo ha sido cargado con exito!"

    def borrar_archivo(self):
        if not self.__archivo_cargado:
            return "El archivo no se ha cargado."

        os.remove(self.__archivo_cargado.name)
        self.__archivo_cargado = None
        return "El archivo se ha borrado exitosamente."

    def agregar_contenido_archivo(self, contenido_a_agregar):
        if not self.__archivo_cargado:
            return "El archivo no se ha cargado."

        self.__archivo_cargado.write(f"{contenido_a_agregar}\n")
        return "Se ha agregado con exito el texto al archivo!"

    def mostrar_contenido_archivo(self):
        if not self.__archivo_cargado:
            return "El archivo no se ha cargado."

        self.__archivo_cargado.seek(0)
        return self.__archivo_cargado.read()

    def mostrar_contenido_de_una_linea_archivo(self, linea_a_leer):
        if not self.__archivo_cargado:
            return "El archivo no se ha cargado."

        self.__archivo_cargado.seek(0)
        archivo_cargado_lineas = self.__archivo_cargado.readlines()
        return f"La linea seleccionada dice: {archivo_cargado_lineas[linea_a_leer]}"
