

from collections import defaultdict, deque
import copy

# ----------------------------------------
# ✅ DEFERRED ACCEPTANCE (DA)
# ----------------------------------------

def algoritmo_da_completo(estudiantes, colegios, capacidades, preferencias, prioridades):
    asignaciones = defaultdict(list)
    propuestas = defaultdict(list)
    siguiente_opcion = {e: 0 for e in estudiantes}
    sin_asignar = deque(estudiantes)

    while sin_asignar:
        estudiante = sin_asignar.popleft()
        if siguiente_opcion[estudiante] >= len(preferencias.get(estudiante, [])):
            continue
        colegio = preferencias[estudiante][siguiente_opcion[estudiante]]
        siguiente_opcion[estudiante] += 1
        propuestas[colegio].append(estudiante)

        def prioridad(c):
            lista = prioridades.get(colegio, [])
            return lista.index(c) if c in lista else len(lista)

        candidatos = sorted(propuestas[colegio], key=prioridad)
        cupo = capacidades.get(colegio, 1)
        asignados = candidatos[:cupo]
        rechazados = candidatos[cupo:]

        asignaciones[colegio] = asignados
        propuestas[colegio] = asignados

        for r in rechazados:
            sin_asignar.append(r)

    resultado = {}
    for colegio, asignados in asignaciones.items():
        for estudiante in asignados:
            resultado[estudiante] = colegio
    return resultado