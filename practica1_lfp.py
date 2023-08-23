inventario = {}

def cargar_inventario():
    """
    Carga el inventario inicial desde un archivo. 
    El formato del archivo debe ser:
    crear_producto <nombre>;<cantidad>;<precio_unitario>;<ubicacion>
    """
    print("Carga del inventario inicial")
    archivo = input("Ingrese la ruta del archivo: ")

    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines()

        for linea in lineas:
            instruccion, datos = linea.strip().split(' ', 1)
            if instruccion == 'crear_producto':
                try:
                    nombre, cantidad, precio_unitario, ubicacion = datos.split(';')
                    clave = (nombre, ubicacion)
                    if "." in cantidad:
                        print(f"Advertencia: La cantidad de '{nombre}' en '{ubicacion}' no es un número entero. Producto no agregado.")
                        continue
                    inventario[clave] = {
                        'cantidad': int(cantidad),
                        'precio unitario': float(precio_unitario),
                    }
                except ValueError:
                    print(f"Error al procesar la línea '{linea.strip()}'. Verifique que los datos son correctos.")
        print("\n¡Inventario cargado con éxito!")
    except FileNotFoundError:
        print("El archivo especificado no existe")
    except Exception as e:
        print("Ocurrió un error al cargar el inventario:", str(e))

def cargar_instrucciones():
    """
    Carga las instrucciones de movimiento desde un archivo. 
    El formato del archivo debe ser:
    agregar_stock <nombre>;<cantidad>;<ubicacion>
    o
    vender_producto <nombre>;<cantidad>;<ubicacion>
    """
    print("Carga las instrucciones de movimiento")
    archivo = input("Ingrese la ruta del archivo:  ")

    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines()

        for linea in lineas:
            instruccion, datos = linea.strip().split(' ', 1)
            nombre, cantidad, ubicacion = datos.split(';')
            clave = (nombre, ubicacion)
            if "." in cantidad:
                print(f"Advertencia: La cantidad para '{nombre}' en '{ubicacion}' no es un número entero. Movimiento no realizado.")
                continue
            cantidad = int(cantidad)

            if instruccion == 'agregar_stock':
                if clave in inventario:
                    inventario[clave]['cantidad'] += cantidad
                else:
                    print(f"Error: El producto {nombre} no existe en {ubicacion}.")
            elif instruccion == 'vender_producto':
                if clave not in inventario:
                    print(f"Error: El producto {nombre} no existe en {ubicacion}.")
                elif inventario[clave]['cantidad'] < cantidad:
                    print(f"Error: No hay suficiente stock de {nombre} en {ubicacion}.")
                else:
                    inventario[clave]['cantidad'] -= cantidad
        print("\n¡Instrucciones procesadas con éxito!")
    except FileNotFoundError:
        print("El archivo especificado no existe")
    except Exception as e:
        print("Ocurrió un error al procesar las instrucciones:", str(e))

def crear_InformeInventario():
    """
    Genera un informe basado en el inventario actual y lo guarda en 'informe.txt'.
    """
    with open("informe.txt", "w", encoding='utf-8') as informe_file:
        informe_file.write("Informe de Inventario:\n")
        informe_file.write("Producto\tUbicación\tCantidad\tPrecio Unitario\tValor Total\n")
        informe_file.write("-" * 90 + "\n")

        for (producto, ubicacion), detalles in inventario.items():
            cantidad = detalles['cantidad']
            precio_unitario = detalles['precio unitario']
            valor_total = cantidad * precio_unitario

            informe_line = "{:<15} {:<10} {:<10} ${:<14.2f} ${:<9.2f}".format(producto, ubicacion, cantidad, precio_unitario, valor_total)
            informe_file.write(informe_line + "\n")

        print("\n¡Informe generado y guardado en 'informe.txt'!")

def salir_programa():
    """
    Sale del programa.
    """
    print("----- Saliendo del programa -----")
    exit()

if __name__ == '__main__':
    while True:
        print("--------------------------------------------------")
        print("Practica 1 - Lenguajes formales y de programación")
        print("--------------------------------------------------")
        print("\n # Sistema de inventario para el programa ")
        print(" 1. Cargar Inventario inicial ")
        print(" 2. Cargar Instrucciones de movimientos ")
        print(" 3. Crear Informe de inventario ")
        print(" 4. Salir ")

        opcion = input("Seleccione la opción que desea:   ")

        if opcion == '1':
            cargar_inventario()
        elif opcion == '2':
            cargar_instrucciones()
        elif opcion == '3':
            crear_InformeInventario()
        elif opcion == '4':
            salir_programa()
        else:
            print("La opción que ingresó en el sistema no es válida. Por favor, ingrese una opción correcta")

        input("Presione Enter para continuar...")
