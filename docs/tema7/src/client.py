"""
Máster Universitario en Ingeniería Informática UGR
Cloud Computing: Fundamentos e Infraestructuras (2020-2021)
Carlos Santiago Sánchez Muñoz
Implementación del cliente
"""

import requests

print(requests.get("http://172.17.0.1:80/", verify=True).json())
