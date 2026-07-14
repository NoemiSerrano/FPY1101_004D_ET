#Diccionarios
recorridos = {
    'R001': ['Santiago', 'Valparaíso', 120, 'normal', 'día', True],
    'R002': ['Santiago', 'Concepción', 500, 'cama', 'noche', True],
    'R003': ['La Serena', 'Coquimbo', 15, 'normal', 'día', False],
    'R004': ['Temuco', 'Valdivia', 165, 'semi-cama', 'día', True],
    'R005': ['Iquique', 'Arica', 310, 'cama', 'noche', False],
    'R006': ['Santiago', 'Rancagua', 90, 'normal', 'día', True],
}

venta = {
    'R001': [7990, 20],
    'R002': [25990, 0],
    'R003': [1990, 35],
    'R004': [12990, 8],
    'R005': [18990, 3],
    'R006': [4990, 12],
}

#Funciones de validación

def validar_numero_entero_positivo(mensaje: str) -> int:
    "Valida que un número sea entero y positivo (mayor que cero)"
    while True:
        try:
            valor = int(input(mensaje))
            if valor == 0:
                print("El valor no puede ser cero.")
            elif valor < 0:
                print("No se pueden ingresar números negativos.")
            else:
                return valor
        except ValueError:
            print("Debe ingresar un número entero válido.")


def validar_string(mensaje: str) -> str:
    "Valida que un texto no esté vacío ni tenga menos de 3 caracteres"
    while True:
        valor = input(mensaje).strip() 
        if len(valor) == 0:
            print("El valor no puede estar vacío.")
        elif len(valor) < 3:
            print("El valor no puede contener menos de 3 caracteres.")
        else:
            return valor


def validar_tipo_bus(tipo: str) -> bool:
    "Valida que el tipo de bus sea'normal', 'semi-cama' o 'cama'"
    return tipo.lower() in ['normal', 'semi-cama', 'cama']


def leer_opcion_menu() -> int:
    "Lee y valida que la opción esté en el rango permitido (1 al 6)"
    while True:
        try:
            opcion = int(input("Ingrese una opción [1-2-3-4-5-6]: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Error: Opción fuera de rango (debe ser de 1 a 6).")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

#Opciones del menu

# Opción 1: Asientos por ciudad de origen
def asientos_origen(origen_buscar: str):
    "Busca los recorridos que parten de la ciudad dada, acumula los asientos y los muestra"
    origen_buscar_clean = origen_buscar.strip().lower()
    total_asientos = 0
    encontrado = False

    for codigo, datos in recorridos.items():
        if datos[0].lower() == origen_buscar_clean:
            encontrado = True
            # Busca los asientos en el diccionario 'venta' usando la misma clave
            if codigo in venta:
                total_asientos += venta[codigo][1]

    if encontrado:
        print(f"Total de asientos disponibles para salidas desde '{origen_buscar}': {total_asientos}")
    else:
        print(f" No se encontraron recorridos saliendo desde '{origen_buscar}'.")


# Opción 2: Búsqueda de recorridos por rango de precio
def buscar_por_rango_precios():
    "Muestra los recorridos con asientos > 0 dentro del rango de precios, ordenados alfabéticamente"
    print("--- Búsqueda por Rango de Precios ---")
    p_min = validar_numero_entero_positivo("Ingrese el precio mínimo: ")
    p_max = validar_numero_entero_positivo("Ingrese el precio máximo: ")

    if p_min > p_max:
        print("Error: El precio mínimo no puede ser mayor que el precio máximo.")
        return

    resultados = []
    for codigo, datos_venta in venta.items():
        precio = datos_venta[0]
        asientos = datos_venta[1]

        if p_min <= precio <= p_max and asientos > 0:
            if codigo in recorridos:
                origen = recorridos[codigo][0]
                destino = recorridos[codigo][1]
                formato = f"{origen}-{destino}--{codigo}"
                resultados.append(formato)

    if resultados:
        resultados.sort()  # Ordenar alfabéticamente
        print(f"Recorridos disponibles en el rango de precios ${p_min} - ${p_max}:")
        for recorrido in resultados:
            print(f" - {recorrido}")
        print()
    else:
        print("No hay recorridos que cumplan las condiciones en ese rango de precios.")


# Opción 3: Actualizar precio de recorrido
def actualizar_precio():
    "Actualiza el precio en el diccionario venta"
    codigo = input("Ingrese el código del recorrido a actualizar (ej: R001): ").strip().upper()
    if codigo not in venta:
        print("Error: El código ingresado no existe.")
        return

    precio_actual = venta[codigo][0]
    print(f"Precio actual para {codigo}: ${precio_actual}")
    nuevo_precio = validar_numero_entero_positivo("Ingrese el nuevo precio: ")

    venta[codigo][0] = nuevo_precio
    print(f"¡Éxito! El precio de {codigo} se actualizó a ${nuevo_precio}.")


# Opción 4: Agregar recorrido
def agregar_recorrido():
    "Agrega un nuevo recorrido asegurando que el código no exista"
    print("--- Registrar Nuevo Recorrido ---")
    codigo = input("Ingrese el nuevo código del recorrido (ej: R007): ").strip().upper() 
    
    if len(codigo) == 0:
        print("Error: El código no puede estar vacío.")
        return
    if codigo in recorridos:
        print("Error: Este código ya se encuentra registrado en el sistema.")
        return

    # Validaciones usando tus funciones corregidas
    origen = validar_string("Ingrese ciudad de origen: ")
    destino = validar_string("Ingrese ciudad de destino: ")
    distancia = validar_numero_entero_positivo("Ingrese distancia en Kilometros: ")

    while True:
        tipo_bus = input("Ingrese tipo de bus (normal/semi-cama/cama): ").strip().lower() 
        if validar_tipo_bus(tipo_bus):
            break
        print("Error: El tipo de bus debe ser 'normal', 'semi-cama' o 'cama'.")

    while True:
        servicio = input("Ingrese servicio (día/noche): ").strip().lower()
        if servicio in ['día', 'dia', 'noche']:
            servicio = 'día' if 'd' in servicio else 'noche'
            break
        print("Error: El servicio debe ser 'día' o 'noche'.")

    while True:
        wifi_op = input("¿Tiene Wi-Fi? (s/n): ").strip().lower()
        if wifi_op in ['s', 'n']:
            tiene_wifi = True if wifi_op == 's' else False
            break
        print("Error: Ingrese únicamente 's' para sí, o 'n' para no.")

    precio = validar_numero_entero_positivo("Ingrese precio del pasaje: ")
    
    while True:
        try:
            asientos = int(input("Ingrese cantidad de asientos disponibles:"))
            if asientos >= 0:
                break
            print("Error: Los asientos no pueden ser negativos.")
        except ValueError:
            print("Error: Debe ingresar un número entero.")

    # Guardar datos en ambos diccionarios
    recorridos[codigo] = [origen, destino, distancia, tipo_bus, servicio, tiene_wifi]
    venta[codigo] = [precio, asientos]
    print(f"¡Éxito! Recorrido {codigo} registrado correctamente.")


# Opción 5: Eliminar recorrido
def eliminar_recorrido():
    "Elimina el recorrido de ambos diccionarios"
    codigo = input("Ingrese el código del recorrido a eliminar (ej: R001): ").strip().upper()
    if codigo not in recorridos:
        print("Error: El código de recorrido no existe en el sistema.")
        return

    confirmar = input(f"¿Seguro que desea eliminar el recorrido {codigo}? (s/n): ").strip().lower()
    if confirmar == 's':
        del recorridos[codigo]
        if codigo in venta:
            del venta[codigo]
        print(f"¡¡Éxito!! Recorrido {codigo} eliminado por completo.")
    else:
        print("Operación cancelada.")
#Menu

def menu():
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("[1] Asientos por ciudad de origen.")
        print("[2] Búsqueda de recorridos por rango de precio.")
        print("[3] Actualizar precio de recorrido.")
        print("[4] Agregar recorrido.")
        print("[5] Eliminar recorrido.")
        print("[6] Salir.")
        print("=====================================")
        
        # Se llama a la función para validar que el rango de la opción sea correcto
        opcion = leer_opcion_menu()

        if opcion == 1:
            ciudad = input("Ingrese la ciudad de origen a buscar: ")
            asientos_origen(ciudad)

        elif opcion == 2:
            buscar_por_rango_precios()

        elif opcion == 3:
            actualizar_precio()

        elif opcion == 4:
            agregar_recorrido()

        elif opcion == 5:
            eliminar_recorrido()

        elif opcion == 6:
            print("Programa finalizado correctamente.")
            break

# Ejecutar programa
menu()