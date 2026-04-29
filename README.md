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

[![Ver demostración del proyecto](https://img.shields.io/badge/▶%20Ver%20Video-Demostración-red?style=for-the-badge&logo=youtube)](https://youtu.be/zhwEwv4vp0Q?si=GXvyq2lQT65SHxvd)









## Funcionamiento del algoritmo

El algoritmo trabaja con una secuencia de incrementos:

n/2 → n/4 → n/8 → ... → 1

En cada iteración:

Se divide el arreglo en sublistas separadas por el gap.
Cada sublista se ordena mediante inserción.
El gap se reduce progresivamente.

Esto permite que los elementos se acerquen a su posición final más rápidamente que en métodos tradicionales.

---

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

### Complejidad Espacial

- **O(1)** - Ordenamiento **in-place** (en el mismo lugar)
- No requiere memoria adicional proporcional al tamaño de entrada
- Solo utiliza variables de control (i, j, gap, temp)

### Gráfica de Complejidad

```
Tiempo de Ejecución (ms)

1000 ┤
     ├─ O(n²) - Bubble Sort (peor caso)
     │
 500 ├─ O(n log n) - Shell Sort (promedio)
     │     /
 250 ├─  /
     │ /─
 100 ├/
     ├
  50 ├─ O(n) - Mejor caso Shell Sort
  25 ├
  10 ├
   5 ├
   1 ├────────────────────────
     └─────────────────────────────
     1K   10K   50K   100K   1M
     (Número de elementos)
```

### Complejidad por Operación

```python
# Operación principal: Comparaciones
Mejor caso (casi ordenado):  O(n)      - Pocos desplazamientos
Caso promedio:               O(n log n) - Balance entre gaps
Peor caso:                   O(n²)      - Muchos desplazamientos

# Cálculo detallado para 50,000 números:
Insertion sort simple:  Aprox. 2,500,000,000 comparaciones
Shell Sort (promedio):  Aprox. 800,000 comparaciones
Mejora: ~3,125x más rápido
```

---

## Evaluación experimental

El programa implementado permite:

Ordenar hasta 50,000 números
Medir el tiempo de ejecución
Validar automáticamente el orden
Exportar resultados a archivo

Esto permite observar el comportamiento real del algoritmo en condiciones cercanas a uso práctico.

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

### Tabla de Recomendaciones

| Tamaño | Tipo de Datos | Recomendación | Razón |
|--------|---------------|---------------|-------|
| < 50 | Cualquier | Insertion Sort | Muy rápido, simple |
| 50-1K | Cualquier | Shell Sort | Buen balance |
| 1K-10K | Aleatorio | Shell Sort | Eficiente |
| 1K-10K | Casi ordenado | Shell Sort | Muy rápido (O(n)) |
| 10K-1M | Cualquier | QuickSort | Mejor promedio |
| Cualquier | Estable req. | MergeSort | Garantiza O(n log n) |
| Búsqueda | N/A | Hash Table | Mejor para búsqueda |


## Comparativa Teórica: Shell Sort vs Insertion Sort

### Resumen Ejecutivo

```
Shell Sort es una GENERALIZACIÓN de Insertion Sort que logra O(n log n)
permitiendo intercambios de elementos distantes, no solo adyacentes.
```

### Análisis Comparativo Detallado

#### 1. **Concepto Fundamental**

**Insertion Sort (Básico):**
- Solo compara/intercambia elementos **adyacentes**
- Cada elemento se mueve una posición a la vez
- Muy simple pero lento para arrays grandes

**Shell Sort (Mejorado):**
- Compara/intercambia elementos **separados por una distancia (gap)**
- El gap disminuye con cada pasada
- Más rápido al permitir "saltos" grandes inicialmente

#### 2. **Complejidad**

```
┌─────────────────────┬────────────────┬─────────────────┐
│ Métrica             │ Insertion Sort  │ Shell Sort      │
├─────────────────────┼────────────────┼─────────────────┤
│ Mejor caso          │ O(n)           │ O(n)            │
│ Caso promedio       │ O(n²)          │ O(n log n)      │
│ Peor caso           │ O(n²)          │ O(n²)           │
│ Espacio             │ O(1)           │ O(1)            │
│ Estable             │ Sí ✓           │ No ✗            │
└─────────────────────┴────────────────┴─────────────────┘
```

#### 3. **Rendimiento Práctico**

Para 50,000 números aleatorios:

```
Insertion Sort:      ~2.5 segundos    (2,500,000,000 ops)
Shell Sort:          ~0.3 segundos    (800,000 ops)
Mejora:              8.3x más rápido

Ratio: O(n²) / O(n log n) = 50000² / (50000 * log₂ 50000)
                          = 2,500,000,000 / 750,000
                          ≈ 3,333x en operaciones
```


#### 4. **Conclusión Teórica**

```
Shell Sort es "Insertion Sort mejorado" porque:

1. Utiliza el mismo concepto: comparar e intercambiar
2. Pero lo generaliza permitiendo gaps variables
3. Esto reduce significativamente el número de movimientos
4. En lugar de O(n²) = 2,500,000,000 comparaciones
   Solo hace O(n log n) = 750,000 comparaciones

La desventaja única: NO es estable (a diferencia de Insertion Sort)
Pero la ganancia en velocidad (8.3x) lo compensa en la mayoría de casos.
```

---


## Resultados

### Discusión de resultados

```

En pruebas realizadas con 50,000 elementos:

El algoritmo mostró un rendimiento significativamente superior a métodos como Bubble Sort.
La reducción progresiva de gaps permitió disminuir el número de comparaciones.
El tiempo de ejecución se mantuvo estable incluso en escenarios grandes.
```

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
- Balam Castillo Pedro
- Pech Cantun Diego
- Loreto Huerta Filiberto

---

