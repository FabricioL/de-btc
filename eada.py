from collections import defaultdict, deque
import copy




def algoritmo_da_con_rechazos(estudiantes, colegios, capacidades, preferencias, prioridades):
    asignaciones = defaultdict(list)
    propuestas = defaultdict(list)
    rechazos = defaultdict(set)
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
            rechazos[colegio].add(r)

    resultado = {}
    for colegio, asignados in asignaciones.items():
        for estudiante in asignados:
            resultado[estudiante] = colegio

    return resultado, rechazos

def eada(estudiantes, colegios, capacidades_orig, preferencias_orig, prioridades_orig):
    # Copiamos estructuras originales para no modificar las de afuera
    capacidades = copy.deepcopy(capacidades_orig)
    preferencias = copy.deepcopy(preferencias_orig)
    prioridades = copy.deepcopy(prioridades_orig)

    asignacion_final = dict()
    estudiantes_restantes = estudiantes.copy()
    colegios_restantes = colegios.copy()

    while True:
        # Paso 1: Ejecutar DA
        asignacion_da, rechazos = algoritmo_da_con_rechazos(
            estudiantes_restantes, colegios_restantes, capacidades, preferencias, prioridades
        )

        # Paso 2: Identificar colegios underdemanded (no rechazaron a nadie)
        underdemanded = [s for s in colegios_restantes if len(rechazos[s]) == 0]

        if not underdemanded:
            # Si no hay más underdemanded, terminamos
            # Los estudiantes restantes se quedan con sus asignaciones del DA
            asignacion_final.update(asignacion_da)
            break

        # Paso 3: Asignar definitivamente los estudiantes en underdemanded
        estudiantes_asignados = []
        for s in underdemanded:
            for i, colegio in asignacion_da.items():
                if colegio == s:
                    asignacion_final[i] = s
                    estudiantes_asignados.append(i)

        # Paso 4: Eliminar colegios y estudiantes del mercado
        colegios_restantes = [s for s in colegios_restantes if s not in underdemanded]
        estudiantes_restantes = [i for i in estudiantes_restantes if i not in estudiantes_asignados]

        for i in estudiantes_restantes:
            preferencias[i] = [s for s in preferencias[i] if s in colegios_restantes]
        for s in colegios_restantes:
            prioridades[s] = [i for i in prioridades[s] if i in estudiantes_restantes]
        for s in underdemanded:
            capacidades[s] = 0  # fuera del mercado

    return asignacion_final