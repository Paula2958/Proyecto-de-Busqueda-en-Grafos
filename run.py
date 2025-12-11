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


# AMPLITUD
ejecutar_busqueda("Amplitud (BFS)",
                  search.breadth_first_graph_search,
                  prob)

# PROFUNDIDAD
ejecutar_busqueda("Profundidad (DFS)",
                  search.depth_first_graph_search,
                  prob)

# RAMIFICACIÓN Y ACOTACIÓN
ejecutar_busqueda("Ramificación y acotación",
                  search.branch_and_bound_graph_search,
                  prob)

# RAMIFICACIÓN Y ACOTACIÓN + SUBESTIMACIÓN
ejecutar_busqueda("Ramificación y acotación con subestimación",
                  search.branch_and_bound_with_underestimation_graph_search,
                  prob)
