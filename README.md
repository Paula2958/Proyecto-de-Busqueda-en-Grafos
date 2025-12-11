# Proyecto de Búsqueda en Grafos

En este proyecto se implementan diferentes tipos de algoritmos de búsqueda en grafos basados.
Incluye:
- Búsqueda en Amplitud o BFS
- Búsqueda en Profundidad o DFS
- Ramificación y Acotación o Branch & Bound
- Ramificación y Acotación con Subestimación o Branch & Bound + heurísitica euclídea

Todos estos algoritmos comparten una única función de búsqueda general (graph_search), diferenciándose solo por el tipo de frontera, es decir, cola utilizada. 

<u>El proyecto sigue esta estructura</u>
.
├── search.py     #Para poder implementar la búsqueda y representación del problema  
├── utils.py     #Script de estructuras auxiliares
└── run.py     #Script principal donde se ejecutan y se prueban las búsquedas.

<u>¿Cómo funciona graph_search?</u>

La función graph_search(problem, fringe) -> Realiza todo el proceso de búsqueda: nodos generados, visitados, poda, control de ciclos y aplicación de heurísiticas cuando es necesario. 

```python
def graph_search(problem, fringe):
    """
    Única función general para:
      - Amplitud (FIFOQueue)
      - Profundidad (Stack)
      - Ramificación y acotación (PriorityQueue)
      - Ramificación y acotación con subestimación (PriorityHQueue)

    Devuelve:
      nodo_solución | None, nodos_generados, nodos_visitados
    """

    closed = set()   # estados ya extraídos de la frontera
    generated = 0
    visited = 0

    # Nodo inicial
    fringe.append(Node(problem.initial), problem)
    generated += 1
    ...


<u>La clave de este diseño es que el comportamiento del algoritmo es determinado por el tipo de frontera:</u>

|Frontera| Clase | Algoritmo |
|-----------|-----------|-----------|
| FIFOQueue | Cola FIFO | Búsqueda en Amplitud (BFS) |
| Stack	Pila | LIFO | Búsqueda en Profundidad (DFS) |
| PriorityQueue | Ordenada por coste g | Ramificación y Acotación | 
| PriorityHQueue | Ordenada por f = g + h | Ramificación y Acotación con Subestimación |


<u>Funcionamiento interno</u>

Graph_search: Inserta el nodo inicial en la frontera; extrae esos nodos según el orden establecido por esa frontera; cuenta el número de nodos generados y visitados y, finalmente, detecta esos estados ya explorados (lista cerrada)

Branch & Bound: Se poda según el coste. En este caso se realizan reemplazos cuando se encuentra un camino más barato al mismo estado.

Branch & Bound con subestimación: Se usa la función f(n) = g(n) + h(n), en la que se almacenan y comparan valores f para los reemplazos.
Cuando se llega al estado objetivo, se calcula el coste total real del camino y se devuelve el nodo solución y sus métricas.



<u>Estructuras de datos de frontera (colas)</u>

En el fichero utils.py se definen las colas personalizadas: 

FIFOQueue → Amplitud (Expande primero los nodos más antiguos.)

Stack → Profundidad (Expande el nodo más reciente.)

PriorityQueue → Ramificación y Acotación (Ordena por coste acumulado g(n).)

PriorityHQueue → Ramificación y Acotación con subestimación (Ordena por f(n) = g(n) + h(n) usando la heurística de distancia euclídea.)

Todas las colas comparten esta interfaz:
```python
append(item, problem)
extend(items, problem)
pop()
__len__()


Esto permite que graph_search funcione con cualquiera de ellas.

<u>El problema GPS (Graph Path Search)</u>

GPSProblem representa el problema de navegar un grafo ponderado (en este caso, el mapa de Rumanía).

Incluye:
1. successor(state) -> devuelve vecinos
2. path_cost -> suma distancias reales del grafo
3. h(node) -> distancia euclídea al objetivo (solo para heurística)


<u>Ejecución de las búsquedas (run.py)</u>

El script run.py realiza:

```python
import time
import search

prob = search.GPSProblem('M', 'F', search.romania)

def ejecutar_busqueda(nombre, funcion_busqueda, problema):
    inicio = time.perf_counter()
    nodo_sol, generados, visitados = funcion_busqueda(problema)
    fin = time.perf_counter()
    tiempo_ms = (fin - inicio) * 1000

    print(f"\n=== {nombre} ===")
    print("Generados:", generados)
    print("Visitados:", visitados)

    if nodo_sol is None:
        print("No se encontró solución.")
    else:
        print("Costo total:", nodo_sol.path_cost)
        print("Ruta:", nodo_sol.path())

    print(f"Tiempo de ejecución: {tiempo_ms:.3f} ms")


ejecutar_busqueda("Amplitud (BFS)",
                  search.breadth_first_graph_search,
                  prob)
ejecutar_busqueda("Profundidad (DFS)",
                  search.depth_first_graph_search,
                  prob)
ejecutar_busqueda("Ramificación y acotación",
                  search.branch_and_bound_graph_search,
                  prob)
ejecutar_busqueda("Ramificación y acotación con subestimación",
                  search.branch_and_bound_with_underestimation_graph_search,
                  prob)


Cuya función es: La medición del tiempo, el cálculo de nodos generados y visitados, la impresión de la ruta óptima y coste total y la ejecución de las 4 estrategias.

La salida por la terminal tendrá esta forma:

=== Ramificación y acotación con subestimación ===
Generados: 25
Visitados: 16
Costo total: 520
Ruta: [<Node F>, <Node S>, <Node R>, <Node C>, <Node D>, <Node M>]
Tiempo de ejecución: 0.055 ms


<u>Obtendrás la tabla completa de métricas.</u>

<img width="781" height="511" alt="Screenshot 2025-12-11 at 10 19 13" src="https://github.com/user-attachments/assets/9f43831f-1103-4813-a7dd-94cd9c515855" />

(Los demás códigos se encuentran en el repositorio)

8. Conclusión del proyecto

Con este proyecto logramos implementar al completo un sistema de búsqueda de grafos con la capacidad suficiente para poder: Explorar el espacio de estados, controlar esos nodos duplicados, realizar las búsquedas más óptimas según el coste, aplicar las heurísticas admisibles, media eficiencia a través de los nodos generados y los visitados.
