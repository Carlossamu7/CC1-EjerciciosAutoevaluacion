"""
Máster Universitario en Ingeniería Informática UGR
Cloud Computing: Fundamentos e Infraestructuras (2020-2021)
Carlos Santiago Sánchez Muñoz
Implementación de la clase Alumno
"""

import re
from typing import List

# Función sacada de https://perezmartin.es/codigo-python-para-comprobar-si-un-dni-nif-o-nie-es-valido/
# Eso comprueba que:
# - Tenga una longitud de 9 dígitos, todos numéricos menos el primero (extranjeros) y
#   el último (control) que pueden estar entre unas letras concretas.
# - Si es extranjero se sustituye la primera letra por su número correspondiente.
# - Se comprueba el dígito de control (última cifra).
def valido_dni(dni: str):
    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
    dig_ext = "XYZ"
    reemp_dig_ext = {'X':'0', 'Y':'1', 'Z':'2'}
    numeros = "1234567890"
    dni = dni.upper()
    if len(dni) == 9:
        dig_control = dni[8]
        dni = dni[:8]
        if dni[0] in dig_ext:
            dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
        return len(dni) == len([n for n in dni if n in numeros]) \
            and tabla[int(dni)%23] == dig_control
    return False

# Comprobación de email válido
# Función sacada de https://micro.recursospython.com/recursos/como-validar-una-direccion-de-correo-electronico.html
body_regex = re.compile('''
    ^(?!\.)                            # name may not begin with a dot
    (
      [-a-z0-9!\#$%&'*+/=?^_`{|}~]     # all legal characters except dot
      |
      (?<!\.)\.                        # single dots only
    )+
    (?<!\.)$                            # name may not end with a dot
''', re.VERBOSE | re.IGNORECASE)
domain_regex = re.compile('''
    (
      localhost
      |
      (
        [a-z0-9]
            # [sub]domain begins with alphanumeric
        (
          [-\w]*                         # alphanumeric, underscore, dot, hyphen
          [a-z0-9]                       # ending alphanumeric
        )?
      \.                               # ending dot
      )+
      [a-z]{2,}                        # TLD alpha-only
   )$
''', re.VERBOSE | re.IGNORECASE)

def valido_email(email: str):
    if not isinstance(email, str) or not email or '@' not in email:
        return False

    body, domain = email.rsplit('@', 1)

    match_body = body_regex.match(body)
    match_domain = domain_regex.match(domain)

    if not match_domain:
        # check for Internationalized Domain Names
        # see https://docs.python.org/2/library/codecs.html#module-encodings.idna
        try:
            domain_encoded = domain.encode('idna').decode('ascii')
        except UnicodeError:
            return False
        match_domain = domain_regex.match(domain_encoded)

    return (match_body is not None) and (match_domain is not None)

class Alumno:
    def __init__(self, nombre: str, email: str, dni :str, lista_asignaturas: List[str]):
        self.__nombre = nombre
        if(valido_email(email)):
            self.__email = email
        else: # Lanza excepción
            raise ValueError("El email no es válido.")
        if(valido_dni(dni)):
            self.__dni = dni
        else: # Lanza excepción
            raise ValueError("El DNI no es válido.")
        self.__lista_asignaturas = lista_asignaturas

    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email

    def get_dni(self):
        return self.__dni

    def get_lista_asignaturas(self):
        return self.__lista_asignaturas

    def set_nombre(self, nombre: str):
        self.__nombre = nombre

    def set_email(self, email: str):
        if(valido_email(email)):
            self.__email = email
        else: # Lanza excepción
            raise ValueError("El email no es válido.")

    # El DNI no cambia, no existe setter.

    def matricula_asignatura(self, asig: str):
        if asig in self.__lista_asignaturas:	# Lanza excepción
            raise ValueError("Asignatura ya matriculada.")
        else:
            self.__lista_asignaturas.append(asig)

    def desmatricula_asignatura(self, asig: str):
        if(asig in self.__lista_asignaturas):
            self.__lista_asignaturas.remove(asig)
        else:	# Lanza excepción
            raise ValueError("No existe tal asignatura.")

    def to_string(self):
        str = "--> " + self.__nombre + " (DNI: " + self.__dni + ", @: " + self.__email + ")" + "\n"
        str += "    Asignaturas: " + ", ".join(self.__lista_asignaturas)
        return str

    def __eq__(self, other):
        return (self.__nombre == other.get_nombre() and
               self.__dni == other.get_dni() and
               self.__email == other.get_email() and
               self.__lista_asignaturas == other.get_lista_asignaturas())
