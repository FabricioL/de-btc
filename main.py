import de as de
import btc as btc
import eada as eada
import json

with open("inputs/estudiantes.json", "r") as f:
    estudiantes = json.load(f)

with open("inputs/colegios.json", "r") as f:
    colegios = json.load(f)

with open("inputs/capacidades.json", "r") as f:
    capacidades = json.load(f)

with open("inputs/preferencias.json", "r") as f:
    preferencias = json.load(f)

with open("inputs/prioridades.json", "r") as f:
    prioridades = json.load(f)

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
