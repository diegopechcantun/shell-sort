# Shell Sort - Proyecto de Estructura de Datos
---

## Descripcion 

El método de ordenamiento Shell consiste en dividir el arreglo (o la lista de elementos) en intervalos (o bloques) de varios elementos para organizarlos después por medio del ordenamiento de inserción directa. El proceso se repite, pero con intervalos cada vez más pequeños, de tal manera que al final, el ordenamiento se haga en un intervalo de una sola posición.

Este proyecto implementa el algoritmo Shell Sort en Python. El programa lee un archivo de texto con 50,000 números enteros y los ordena de forma ascendente o descendente, midiendo el tiempo de ejecución en segundos y milisegundo


---

## Integrantes

- **Balam Castillo Pedro**
- **Pech Cantun Diego**
- **Loreto Huerta Filiberto**

---

## Estructura del Repositorio

```
shell-sort-proyecto/
│
├── shell.py
├── datos.txt
├── resultado.txt
└── README.md
```
---
## Video demostrativo

### Video subido a YouTube 

[![Ver demostración del proyecto](https://img.shields.io/badge/▶%20Ver%20Video-Explicación-red?style=for-the-badge&logo=youtube)](https://youtu.be/zhwEwv4vp0Q?si=GXvyq2lQT65SHxvd)


## Análisis de Complejidad

### Complejidad Temporal

| Caso | Complejidad | Descripción |
|------|-------------|-------------|
| **Mejor caso** | **O(n)** | Cuando el arreglo está casi ordenado |
| **Caso promedio** | **O(n log n)** | Depende de la secuencia de intervalos |
| **Peor caso** | **O(n²)** | Con la secuencia original de Shell n/2, n/4,... |

### Análisis Detallado de O(n log n) promedio

La complejidad promedio de **O(n log n)** se logra cuando se utiliza una buena secuencia de intervalos como la de **Knuth**: (3^k - 1)/2.

**Demostración:**
```
Para cada gap h:
  - Hacemos insertion sort en subarreglos de tamaño n/h
  - Costo: O((n/h)²) por subarreglo, pero optimizado

Con la secuencia de Knuth:
  - Número de gaps: O(log n)
  - Costo total: O(n log n) en caso promedio
```


## Casos de Uso

### Cuándo usar Shell Sort

1. **Arreglos de tamaño medio** (1,000 - 50,000 elementos)
   - Ejemplo: Ordenar registros de una base de datos pequeña
   - Ventaja: Mejor que insertion sort, más simple que quicksort

2. **Cuando se requiere ordenamiento in-place**
   - Ejemplo: Dispositivos con memoria limitada
   - Ventaja: No necesita memoria adicional O(n)

3. **Datos parcialmente ordenados**
   - Ejemplo: Lista de estudiantes por calificación que recibe actualizaciones
   - Ventaja: Complejidad cercana a O(n) si está casi ordenado

4. **Implementaciones educativas**
   - Ejemplo: Enseñanza de algoritmos de ordenamiento
   - Ventaja: Más complejo que bubble sort, más simple que quicksort

5. **Cuando la simplicidad es importante**
   - Ejemplo: Lenguajes de programación limitados
   - Ventaja: Implementación simple (~20 líneas)

### Cuándo NO usar Shell Sort

1. **Arreglos muy grandes** (>100,000 elementos)
   - Usar: QuickSort, MergeSort, HeapSort
   - Razón: Peor complejidad que O(n log n) en algunos casos

2. **Cuando se requiere estabilidad**
   - Usar: MergeSort, BubbleSort
   - Razón: Shell Sort no preserva orden relativo de elementos iguales

3. **Datos completamente aleatorios**
   - Usar: QuickSort
   - Razón: QuickSort es más eficiente en este caso

4. **Búsqueda frecuente en datos (online)**
   - Usar: B-Trees, Hash Tables
   - Razón: No es apropiado para búsqueda



## Comparativa Teórica: Shell Sort vs Bubble Sort


### Análisis Comparativo Detallado

####  **Complejidad**

```
| Característica      |   Shell Sort      |   Bubble Sort     |
|---------------------|-------------------|-------------------|
| Complejidad         | ~O(n^1.3)         | O(n²)             |
| Comparaciones       | Reducidas         | Muy altas         |
| Intercambios        | Eficientes        | Ineficientes      |
| Uso real            | Práctico          | Educativo         |
```

#### **Análisis**


Bubble Sort compara elementos adyacentes repetidamente, lo que genera una gran cantidad de operaciones redundantes.

Shell Sort mejora esto al comparar elementos distantes, reduciendo drásticamente la cantidad de iteraciones necesarias.

Para 50,000 datos:
- Bubble Sort: tiempo excesivo (no viable)
- Shell Sort: ~0.4 segundos
  

---
## Conclusión

Shell Sort representa un equilibrio entre simplicidad y eficiencia.
Aunque no supera a algoritmos avanzados como Quick Sort, sigue siendo una opción viable cuando se requiere:

Bajo consumo de memoria
Implementación sencilla
Mejor rendimiento que algoritmos básicos

Este proyecto demuestra su utilidad práctica en el procesamiento de datos de tamaño medio.


---

## Créditos

**Proyecto Académico**
- Institución: Instituto Tecnológico de Mérida
- Curso: Estructura de Datos
- Programa: Ingeniería en Sistemas Computacionales

**Referencias:**
- UAPA-CUAED UNAM - Material educativo
- Cormen, Leiserson, Rivest, Stein - "Introduction to Algorithms"
- Sedgewick, Wayne - "Algorithms (4th Edition)"

---

## Contacto

Para preguntas o sugerencias, contactar a los integrantes del equipo:
- Balam Castillo Pedro - 
- Pech Cantun Diego - 
- Loreto Huerta Filiberto - 

---

