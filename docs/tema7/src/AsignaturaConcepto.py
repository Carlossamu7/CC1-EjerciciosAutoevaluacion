"""
Máster Universitario en Ingeniería Informática UGR
Cloud Computing: Fundamentos e Infraestructuras (2020-2021)
Carlos Santiago Sánchez Muñoz
Implementación de la clase AsignaturaConcepto
"""

class AsignaturaConcepto:
    def __init__(self, id: str, nombre_asignatura: str, curso: int, concepto: str):
        self.__id = id
        self.__nombre_asignatura = nombre_asignatura
        self.__curso = curso
        self.__concepto = concepto

    def get_id(self):
        return self.__id

    def get_nombre_asignatura(self):
        return self.__nombre_asignatura

    def get_curso(self):
        return self.__curso

    def get_concepto(self):
        return self.__concepto

    def to_string(self):
        str = "--> " + self.__nombre_asignatura + " (" + self.__id + ")\n"
        str += "    Curso: {}".format(self.__curso) + "\n"
        str += "    Concepto: " + self.__concepto
        return str

    def __eq__(self, other):
        return (self.__id == other.get_id() and
               self.__nombre_asignatura == other.get_nombre_asignatura() and
               self.__curso == other.get_curso() and
               self.__concepto == other.get_concepto())
