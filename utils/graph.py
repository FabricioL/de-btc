
import networkx as nx
import matplotlib.pyplot as plt


def visualizar_grafo_señalamientos(grafo, ciclos, ronda):
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(grafo, seed=42)
    colores = []

    for nodo in grafo.nodes:
        if any(nodo in ciclo for ciclo in ciclos):
            colores.append("lightcoral")
        else:
            colores.append("lightblue")

    nx.draw(grafo, pos, with_labels=True, node_color=colores, node_size=2000, font_size=10, arrows=True)
    nx.draw_networkx_edges(grafo, pos, arrows=True)
    plt.title(f"Grafo de señalamiento - Ronda {ronda}")
    plt.show()

def encontrar_colegio_objetivo(e, asignacion, preferencias, colegios_retirados):
    asignado = asignacion[e]
    pref_e = preferencias[e]
    pos = pref_e.index(asignado)
    for i in range(pos-1, -1, -1):
        c = pref_e[i]
        if c not in colegios_retirados:
            return c
    return None

def construir_grafo(estudiantes_activos, asignacion, preferencias, prioridades, asignaciones_colegios, colegios_retirados):
    G = nx.DiGraph()
    for e in estudiantes_activos:
        c_objetivo = encontrar_colegio_objetivo(e, asignacion, preferencias, colegios_retirados)
        if not c_objetivo:
            continue
        candidatos = asignaciones_colegios[c_objetivo]
        if len(candidatos) == 0:
            continue
        elif len(candidatos) == 1:
            e2 = candidatos[0]
        else:
            # Elegimos el de mayor prioridad para ese colegio
            orden = prioridades[c_objetivo]
            candidatos_ordenados = sorted(candidatos, key=lambda x: orden.index(x) if x in orden else len(orden))
            e2 = candidatos_ordenados[0]
        G.add_edge(e, e2)
    return G

def encontrar_ciclos(grafo):
    ciclos = []
    try:
        while True:
            ciclo = nx.find_cycle(grafo, orientation="original")
            nodos = [x[0] for x in ciclo]
            if nodos not in ciclos:
                ciclos.append(nodos)
            for n in nodos:
                grafo.remove_node(n)
    except:
        pass
    return ciclos