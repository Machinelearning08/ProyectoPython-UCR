import os
from time import sleep

from manipular_archivo import ManipularArchivo


def app():

    salida = False
    print("==== Tarea Programada Numero 3 ====")
    print("==== Jeremy Calderon Baltodano ====\n")
    print("==== Cargando... ====\n")
    sleep(2)
    ma = ManipularArchivo()

    while not salida:
        _ = os.system('clear') if os.name == 'posix' else os.system('cls')
        print("\n")
        print("1. Cargar archivo")
        print("2. Borrar el archivo")
        print("3. Agregar contenido al archivo")
        print("4. Mostrar todo el contenido del archivo")
        print("5. Mostrar el contenido de una línea específica")
        print("6. Salir")
        print("\n")

        try:
            respuesta = int(input("Digite la opción que desee realizar: "))
        except ValueError as e:
            print("El valor ingresado no es valido. Por favor ingrese de nuevo otro valor.\n")
            sleep(2)
            continue
        except Exception as e:
            print("Ha ocurrido un error mientras usted digitaba el valor.\n")
            sleep(2)
            continue

        if respuesta == 1:
            try:
                ruta_del_archivo = str(input("Ingrese la ruta del archivo que desea cargar: "))
                print(ma.cargar_archivo(ruta_del_archivo))
            except Exception as e:
                print(f"Ha ocurrido un error cargando el archivo: {str(e)}.\n")

        elif respuesta == 2:
            try:
                print(ma.borrar_archivo())
            except Exception as e:
                print(f"Ha ocurrido un error borrando el archivo: {str(e)}.\n")

        elif respuesta == 3:
            try:
                contenido_a_agregar = str(input("Ingrese el texto que desee agregarle a su archivo: "))
                print(ma.agregar_contenido_archivo(contenido_a_agregar))
            except Exception as e:
                print(f"Ha ocurrido un error escribiendo en el archivo: {str(e)}.\n")

        elif respuesta == 4:
            try:
                print(ma.mostrar_contenido_archivo())
            except Exception as e:
                print(f"Ha ocurrido un error mostrando el archivo: {str(e)}.\n")

        elif respuesta == 5:
            try:
                linea_a_leer = int(input("Ingrese el numero de la linea que desea leer: "))
                print(ma.mostrar_contenido_de_una_linea_archivo(linea_a_leer))
            except IndexError as e:
                print("La linea ingresada no existe.")

            except ValueError as e:
                print(f"Ingrese un número valido.")

            except Exception as e:
                print(f"Ha ocurrido un error obteniendo la linea que desea leer.")

        elif respuesta == 6:
            print("Ha salido con exito. Muchas gracias por utilizar mi software.")
            salida = True

        input("Presione enter para continuar...")


if __name__ == '__main__':
    app()
