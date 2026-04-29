'''Estructura de datos, Ingeniería en sistemas computacionales 
Métodos de ordenamiento
Integrantes:
Balam Castillo Pedro
Pech Cantun Diego
Loreto Huerta Filiberto
'''
#Importación de los modulos
import time
import os

# Algoritmo Shell Sort
def shell_sort(arreglo,orden_ascendiente=True):
    longitud_arreglo = len(arreglo)
    gap = longitud_arreglo // 2

    while gap > 0:
        for i in range(gap, longitud_arreglo):
            valor_temporal = arreglo[i]
            posicion_valor = i

            if orden_ascendiente:
                while posicion_valor >= gap and arreglo[posicion_valor - gap] > valor_temporal:
                    arreglo[posicion_valor] = arreglo[posicion_valor - gap]
                    posicion_valor -= gap
            else:
                while posicion_valor >= gap and arreglo[posicion_valor - gap] < valor_temporal:
                    arreglo[posicion_valor] = arreglo[posicion_valor - gap]
                    posicion_valor -= gap

            arreglo[posicion_valor] = valor_temporal
        gap //= 2

    return arreglo

#Verificador de si un arreglo esta correctamente ordenado.
def verificar_orden(arreglo, ascendente=True):
    
    if len(arreglo) <= 1:
        return True
    
    for i in range(len(arreglo) - 1):
        if ascendente:
            if arreglo[i] > arreglo[i + 1]:
                return False
        else:
            if arreglo[i] < arreglo[i + 1]:
                return False
    return True

# Leer archivo y extraer numeros
def leer_archivo(nombre_archivo):
    numeros = []
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        
        for linea in lineas:
            linea = linea.strip()
            if linea:
                numeros.append(int(linea))
    return numeros

# Programa principal
def main():
    print("Sistema Shell sort")
    
#Busqueda del archivo para ordenar
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    
    posibles_nombres = ["datos.txt", "datos"]
    archivo_encontrado = None
    
#Cuando el archivo es encontrado
    for nombre in posibles_nombres:
        ruta_completa = os.path.join(carpeta_actual, nombre)
        if os.path.exists(ruta_completa):
            archivo_encontrado = ruta_completa
            print(f"Archivo encontrado: {nombre}")
            break
    
#Verificación y mensaje por si hay errores con el archivo
    if archivo_encontrado is None:
        print("Error: No se encontró el archivo 'datos.txt' ni 'datos'")
        print(f"Buscando en: {carpeta_actual}")
        return
    
    try:
#Verificación si hay discrepancia en los numeros mencionados con los recibidos
        numeros = leer_archivo(archivo_encontrado)
        if len(numeros) != 50000:
            print(f"Error, Se esperaban 50000 numeros, pero el archivo tiene {len(numeros)} numeros")
        print(f"Se cargaron {len(numeros):,} numeros.")
    except ValueError:
        print("Error: El archivo contiene datos no numericos")
        return

#Selección de secuencia para el ordenamiento de numeros
    print("\nComo deseas ordenar los numeros?")
    print("(1) Ascendente")
    print("(2) Descendente")
    
    opcion = input("Selecciona una opcion (1 o 2): ").strip()

#Verificación de errores si se introduce un caracter invalido en el terminal
    while opcion != "1" and opcion != "2":
        print("Opcion invalida.")
        opcion = input("Selecciona una opcion (1 o 2): ").strip()
    if opcion == "1":
        ascendente = True
    else:
        ascendente = False      

#Medición de tiempo de ordenamiento
    inicio = time.time()
    datos_a_ordenar = numeros.copy()
    numeros_ordenados = shell_sort(datos_a_ordenar, ascendente)
    fin = time.time()

    tiempo_s = (fin - inicio) 
    tiempo_ms = (fin- inicio) *1000

#Impresiones del tiempo de ordenamiento
    print("\nOrdenamiento completado.")
    print(f"Tiempo de ejecucion: {tiempo_s:.2f} segundos(redondeado) o {tiempo_ms:.2f} milisegundos(preciso).")

#Indicador del estado de ordenamiento
    if verificar_orden(numeros_ordenados, ascendente):
        print("Verificacion: El orden es correcto")
    else:
        print("ADVERTENCIA: Error en el ordenamiento")

#Impresiones de los primeros caracteres en el orden
    print("\nPrimeros 10 numeros ordenados:")
    print(numeros_ordenados[:10])

#creación de archivo de datos ordenados
    ruta_salida = os.path.join(carpeta_actual, "resultado.txt")
    with open(ruta_salida, "w") as f:
        for num in numeros_ordenados:
            f.write(str(num) + "\n")

    print(f"\nArchivo 'resultado.txt' generado en: {carpeta_actual}")

#ejecutor de metodo main
if __name__ == "__main__":
    main()