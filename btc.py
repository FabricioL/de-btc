import utils.graph as graph_utils
from collections import defaultdict, deque
import copy

def btc_post_da(estudiantes, colegios, capacidades, preferencias, prioridades, asignacion_da):
    asignacion = copy.deepcopy(asignacion_da)
    asignaciones_colegios = defaultdict(list)
    for e, c in asignacion.items():
        asignaciones_colegios[c].append(e)

    estudiantes_satisfechos = {e for e in estudiantes if e in asignacion.keys() and e in preferencias.keys() and preferencias[e][0] == asignacion[e]}
    estudiantes_activos = [e for e in estudiantes if e in asignacion.keys() and e in preferencias.keys() and e not in estudiantes_satisfechos]
    colegios_retirados = set()

    ronda = 1
    while True:
        print(f"\n🔁 Ronda {ronda}")

        # Retiramos colegios que llenaron su cupo con primeras opciones
        for c in colegios:
            asignados = asignaciones_colegios[c]
            primeros = [e for e in asignados if e in asignacion.keys() and e in preferencias.keys() and preferencias[e][0] == c]
            if len(primeros) == capacidades[c]:
                colegios_retirados.add(c)
                print(f"🏫 Colegio retirado: {c}")

        # Construcción del grafo de señalamiento
        grafo = graph_utils.construir_grafo(estudiantes_activos, asignacion, preferencias, prioridades, asignaciones_colegios, colegios_retirados)
        ciclos = graph_utils.encontrar_ciclos(grafo.copy())

        graph_utils.visualizar_grafo_señalamientos(grafo, ciclos, ronda)

        if not ciclos:
            print("✅ No hay más ciclos. Terminamos.")
            break

        # Realizar mejoras por cada ciclo
        for ciclo in ciclos:
            n = len(ciclo)
            nuevos = {}
            for i in range(n):
                e_origen = ciclo[i]
                e_destino = ciclo[(i+1)%n]
                colegio_nuevo = asignacion[e_destino]
                nuevos[e_origen] = colegio_nuevo

            for e, c_nuevo in nuevos.items():
                c_viejo = asignacion[e]
                asignacion[e] = c_nuevo
                asignaciones_colegios[c_viejo].remove(e)
                asignaciones_colegios[c_nuevo].append(e)

        # Actualizamos la lista de estudiantes activos
        estudiantes_satisfechos = {e for e in estudiantes if e in asignacion.keys() and e in preferencias.keys() and preferencias[e][0] == asignacion[e]}
        estudiantes_activos = [e for e in estudiantes if e in asignacion.keys() and e in preferencias.keys() and e not in estudiantes_satisfechos]

        ronda += 1

    return asignacion