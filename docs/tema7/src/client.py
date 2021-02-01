"""
Máster Universitario en Ingeniería Informática UGR
Cloud Computing: Fundamentos e Infraestructuras (2020-2021)
Carlos Santiago Sánchez Muñoz
Implementación del cliente
"""

import requests

print(requests.get("http://localhost:4000/", verify=True).json())
#print(requests.get("http://localhost:4000/alumnos", verify=True).json())
#print(requests.get("http://localhost:4000/asignaturas", verify=True).json())
