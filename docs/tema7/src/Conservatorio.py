"""
Máster Universitario en Ingeniería Informática UGR
Cloud Computing: Fundamentos e Infraestructuras (2020-2021)
Carlos Santiago Sánchez Muñoz
Implementación de la clase Conservatorio
"""

import sys
sys.path.append('src')
from typing import List

from Alumno import Alumno
from Asignatura import Asignatura

class Conservatorio:
    def __init__(self):
        self.nombre_conservatorio = "MiConservatorio"
        self.__dic_alumnos = {}     # Diccionario
        self.__dic_asignaturas = {}     # Diccionario

    def get_nombre_conservatorio(self):
        return self.nombre_conservatorio

    def get_diccionario_alumnos(self):
        return self.__dic_alumnos

    def get_numero_alumnos(self):
        return len(self.__dic_alumnos)

    def get_diccionario_asignaturas(self):
        return self.__dic_asignaturas

    def get_numero_asignaturas(self):
        return len(self.__dic_asignaturas)

    ###############
    ### Alumnos ###
    ###############

    def exist_alumno(self, dni: str):
        if dni in self.__dic_alumnos:
            return True
        else:
            return False

    def dar_alta_alumno(self, nombre: str, email: str, dni: str, asignaturas: List[str]):
        if(self.exist_alumno(dni)):
            raise ValueError("Ya existe un alumno con este DNI.")
        else:
            # En caso de DNI o email inválido se levanta una expeción
            alumno = Alumno(nombre, email, dni, asignaturas)
            self.__dic_alumnos[dni] = alumno

    def get_alumno(self, dni: str):
        if self.exist_alumno(dni):
            return self.__dic_alumnos[dni]
        else:
            return "No existe ningún alumno con ese DNI."

    def get_alumnos_nombre(self, nombreAlum: str):
        list = []
        for alum in self.__dic_alumnos:
            if(self.__dic_alumnos[alum].get_nombre()==nombreAlum):
                list.append(self.__dic_alumnos[alum].get_dni())
        return list

    def get_horario_asignatura_alumno(self, dni: str, asignatura: str):
        if(self.exist_alumno(dni)):
            alum = self.__dic_alumnos[dni]
            if (asignatura in alum.get_lista_asignaturas()):
                for asi in self.__dic_asignaturas:
                    if(self.__dic_asignaturas[asi].get_nombre_asignatura()==asignatura):
                        return self.__dic_asignaturas[asi].get_horario()
            else:
                return "Este alumno no está matriculado en esa asignatura."

        else:
            return "No existe ningún alumno con ese DNI."

    def get_aula_asignatura_alumno(self, dni: str, asignatura: str):
        if(self.exist_alumno(dni)):
            alum = self.__dic_alumnos[dni]
            if (asignatura in alum.get_lista_asignaturas()):
                for asi in self.__dic_asignaturas:
                    if(self.__dic_asignaturas[asi].get_nombre_asignatura()==asignatura):
                        return self.__dic_asignaturas[asi].get_aula()
            else:
                return "Este alumno no está matriculado en esa asignatura."

        else:
            return "No existe ningún alumno con ese DNI."

    def get_horario_alumno(self, dni: str):
        list = []
        if(self.exist_alumno(dni)):
            alum = self.__dic_alumnos[dni]
            for asig in alum.get_lista_asignaturas():
                for asi in self.__dic_asignaturas:
                    if(self.__dic_asignaturas[asi].get_nombre_asignatura()==asig):
                        list.append(self.__dic_asignaturas[asi].get_horario())
            return list
        else:
            return "No existe ningún alumno con ese DNI."

    def get_aulas_alumno(self, dni: str):
        list = []
        if(self.exist_alumno(dni)):
            alum = self.__dic_alumnos[dni]
            for asig in alum.get_lista_asignaturas():
                for asi in self.__dic_asignaturas:
                    if(self.__dic_asignaturas[asi].get_nombre_asignatura()==asig):
                        if(not self.__dic_asignaturas[asi].get_aula() in list):
                            list.append(self.__dic_asignaturas[asi].get_aula())
            return list
        else:
            return "No existe ningún alumno con ese DNI."

    ###################
    ### Asignaturas ###
    ###################

    def exist_asignatura(self, id: str):
        if id in self.__dic_asignaturas:
            return True
        else:
            return False

    def dar_alta_asignatura(self, id: str, nombre_asignatura: str, curso: int, concepto: str, profesor: str, horario: str, aula: str):
        if(self.exist_asignatura(id)):
            raise ValueError("Ya existe esta asignatura.")
        else:
            self.__dic_asignaturas[id] = Asignatura(id, nombre_asignatura, curso, concepto, profesor, horario, aula)

    def borrar_asignatura(self, id: str):
        if(self.exist_asignatura(id)):
            del self.__dic_asignaturas[id]
        else:
            raise ValueError("No existe esta asignatura.")

    def get_asignatura(self, id: str):
        if self.exist_asignatura(id):
            return self.__dic_asignaturas[id]
        else:
            return "No existe la asignatura con ID " + id + "."

    def get_lista_asignaturas_profesor(self, profesor: str):
        list = []
        for asig in self.__dic_asignaturas:
            if(self.__dic_asignaturas[asig].get_profesor()==profesor):
                list.append(self.__dic_asignaturas[asig])
        return list

    def get_nombre_asignaturas_profesor(self, profesor: str):
        list = []
        asigProf = self.get_lista_asignaturas_profesor(profesor)
        for asig in asigProf:
            list.append(asig.get_nombre_asignatura())
        return list

    def get_horario_profesor(self, profesor: str):
        list = []
        asigProf = self.get_lista_asignaturas_profesor(profesor)
        for asig in asigProf:
            list.append(asig.get_horario())
        return list

    def get_aulas_profesor(self, profesor: str):
        list = []
        asigProf = self.get_lista_asignaturas_profesor(profesor)
        for asig in asigProf:
            if(not asig.get_aula() in list):
                list.append(asig.get_aula())
        return list

    def to_string(self):
        str = "¡Bienvenido a " + self.get_nombre_conservatorio() + "!\n\n"

        str += "--------------    ALUMNOS    --------------\n\n"
        for alum in self.__dic_alumnos:
            str += self.__dic_alumnos[alum].to_string()
            str += "\n"
        str += "\n\n"

        str += "--------------  ASIGNATURAS  --------------\n\n"
        for asig in self.__dic_asignaturas:
            str += self.__dic_asignaturas[asig].to_string()
            str += "\n"
        return str

# Función que crea el Conservatorio a partir del json
def crea_conservatorio(data):
    # Creando el conservatorio
    conser = Conservatorio()

    # Dando de alta a los alumnos existentes
    for i in range(len(data["alumnos"])):
        conser.dar_alta_alumno(data["alumnos"][i]["nombre"],
                               data["alumnos"][i]["email"],
                               data["alumnos"][i]["dni"],
                               [asig for asig in data["alumnos"][i]["lista_asignaturas"]])

    # Dando de alta las asignaturas existentes
    for i in range(len(data["asignaturas"])):
        conser.dar_alta_asignatura(data["asignaturas"][i]["id"],
                                   data["asignaturas"][i]["nombre_asignatura"],
                                   data["asignaturas"][i]["curso"],
                                   data["asignaturas"][i]["concepto"],
                                   data["asignaturas"][i]["profesor"],
                                   data["asignaturas"][i]["horario"],
                                   data["asignaturas"][i]["aula"])

    return conser
