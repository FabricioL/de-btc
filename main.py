import de as de
import btc as btc
import eada as eada
# Lista de estudiantes
estudiantes = ['i_1', 'i_2', 'i_3', 'i_4','i_5','i_6','i_7','i_8']

# Lista de colegios
colegios = ['s_1', 's_2', 's_3', 's_4', 's_5', 's_6', 's_7']
capacidades = {'s_1': 1, 's_2': 1, 's_3':1 ,'s_4':1, 's_5':1, 's_6':1, 's_7':2}

# Preferencias de cada estudiante (de mejor a peor)
preferencias = {
    'i_1': ['s_1', 's_4', 's_7', 's_2', 's_3', 's_5','s_6'],
    'i_2': ['s_1', 's_4', 's_2', 's_3', 's_5', 's_6','s_7'],
    'i_3': ['s_1', 's_2', 's_3', 's_4', 's_5', 's_6','s_7'],
    'i_4': ['s_4', 's_3', 's_1', 's_2', 's_5', 's_6','s_7'],
    'i_5': ['s_4', 's_7', 's_1', 's_2', 's_3', 's_5','s_6'],
    'i_6': ['s_4', 's_5', 's_7', 's_2', 's_3', 's_1','s_2'],
    'i_7': ['s_1', 's_5', 's_6', 's_2', 's_3', 's_4','s_7'],
    'i_8': ['s_1', 's_6', 's_4', 's_2', 's_3', 's_5','s_7']
}

# Prioridades de los colegios (a quién prefieren aceptar primero)
prioridades = {
    's_1': ['i_4', 'i_1', 'i_2','i_3', 'i_7', 'i_5','i_8', 'i_6'],
    's_2': ['i_2', 'i_3'],
    's_3': ['i_3', 'i_4'],
    's_4': ['i_8', 'i_5', 'i_6','i_7', 'i_2', 'i_1','i_4', 'i_3'],
    's_5': ['i_6', 'i_7'],
    's_6': ['i_7', 'i_8'],
    's_7': ['i_5']

}

# Ejecutar DA
asignacion_da = de.algoritmo_da_completo(estudiantes, colegios, capacidades, preferencias, prioridades)

# Ejecutar BTC con mejoras
asasignacion_mejorada = btc.btc_post_da(estudiantes, colegios, capacidades, preferencias, prioridades, asignacion_da)

# Ejecutar Efficiency-adjusted deferred acceptance mechanism
asignacion_eada = eada.eada(estudiantes, colegios, capacidades, preferencias, prioridades)

print("📋 Resultado del DA:")
for e in estudiantes:
    print(f"{e} → {asignacion_da.get(e)}")


print("\n📋 Asignación final mejorada:")
for estudiante in sorted(asasignacion_mejorada):
    print(f"{estudiante} → {asasignacion_mejorada[estudiante]}")

print("\n📋 Resultado del EADA:")
for e in estudiantes:
    print(f"{e} → {asignacion_eada.get(e)}")
