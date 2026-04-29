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

## Proyecto Académico
- Institución: Instituto Tecnológico de Mérida
- Materia: Estructura de Datos
- Carrera: Ingeniería en Sistemas Computacionales


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
| **Peor caso** | **O(n²)** |Se presenta cuando los datos están en el orden más desfavorable. |

---
## Casos de Uso

### Cuándo usar Shell Sort

1. **Cuando se trabaja con arreglos medianos (no tan grandes como para usar algoritmos más complejos).
2. **Cuando los datos están parcialmente ordenados.
3. **Cuando se necesita un algoritmo simple de implementar pero más eficiente que métodos básicos como Bubble Sort.
4. **Cuando se requiere bajo uso de memoria (ya que no usa memoria extra).

### Cuándo NO usar Shell Sort

1. **Se manejan grandes volúmenes de datos (como 50,000+ elementos).
2. **Se requiere máxima eficiencia garantizada.
3. **Se necesita un algoritmo estable.
---


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


## Comparativa Teórica: Shell Sort vs Quick Sort

```
Shell Sort vs Quick Sort

| Característica        | Shell Sort         | Quick Sort        |

|---------------------|-------------------|-------------------|

| Complejidad promedio| ~O(n^1.3)         | O(n log n)        |

| Peor caso           | O(n²)             | O(n²)             |

| Rendimiento real    | Bueno             | Muy alto          |

| Localidad de cache  | Alta              | Media             |

| Sensibilidad        | Baja              | Alta (pivote)     |
```

**Análisis técnico:**

Quick Sort es generalmente el algoritmo más rápido en la práctica debido a su complejidad promedio O(n log n). Sin embargo, su rendimiento depende de una buena elección del pivote.

Shell Sort:

- No depende de decisiones dinámicas (como pivote)

- Es más predecible en ejecución

- Menos propenso a degradarse por casos específicos


---
## Conclusión

Shell Sort representa un equilibrio entre simplicidad y eficiencia.
Aunque no supera a algoritmos avanzados como Quick Sort, sigue siendo una opción viable cuando se requiere:

Bajo consumo de memoria
Implementación sencilla
Mejor rendimiento que algoritmos básicos

Este proyecto demuestra su utilidad práctica en el procesamiento de datos de tamaño medio.


---

## Contacto

Para preguntas o sugerencias, contactar a los integrantes del equipo:
- Balam Castillo Pedro - 
- Pech Cantun Diego - 
- Loreto Huerta Filiberto - 

---

