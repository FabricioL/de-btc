import de as de
import btc as btc
import eada as eada
import json

caso="ejemplo4"


with open(caso+"/estudiantes.json", "r") as f:
    estudiantes = json.load(f)

with open(caso+"/colegios.json", "r") as f:
    colegios = json.load(f)

with open(caso+"/capacidades.json", "r") as f:
    capacidades = json.load(f)

with open(caso+"/preferencias.json", "r") as f:
    preferencias = json.load(f)

with open(caso+"/prioridades.json", "r") as f:
    prioridades = json.load(f)

# Ejecutar DA
asignacion_da = de.algoritmo_da_completo(estudiantes, colegios, capacidades, preferencias, prioridades)

# Ejecutar BTC con mejoras
asignacion_btcda = btc.btc_post_da(estudiantes, colegios, capacidades, preferencias, prioridades, asignacion_da)

# Ejecutar Efficiency-adjusted deferred acceptance mechanism
asignacion_eada = eada.eada(estudiantes, colegios, capacidades, preferencias, prioridades)

print("📋 Resultado del DA:")
for e in estudiantes:
    print(f"{e} → {asignacion_da.get(e)}")


print("\n📋 Asignación final mejorada:")
for e in estudiantes:
    print(f"{e} → {asignacion_btcda[e]}")

print("\n📋 Resultado del EADA:")
for e in estudiantes:
    print(f"{e} → {asignacion_eada.get(e)}")


print("¿DA es igual a ¿BTCDA?", asignacion_da == asignacion_btcda)
print("¿BTCDA es igual a EADA?", asignacion_btcda == asignacion_eada)