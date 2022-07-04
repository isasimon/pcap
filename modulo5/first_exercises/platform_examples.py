"""
Módulos útiles: platform

Permite acceder a datos sobre el sistema operativo,
el hardware e info sobre el intérprete.
"""

from platform import platform as pf, machine, processor, \
    system, version, python_implementation, python_version_tuple

print(pf())
print(pf(aliased=1))  # aliased devuelvería nombres de capas subyacentes alternativos
print(pf(aliased=0, terse=1))  # terse devuelve un nombre abreviado

print(machine())  # Devuelve el nombre genérico del procesador
print(processor())  # Devuelve el nombre real del proccesador
print(system())  # Devuelve el nombre genérico del sistema operativo
print(version())  # Devuelve la version del SO

print(python_implementation())  # Implementación de Python (normalmente CPython)
print(python_version_tuple())  # Version de python




