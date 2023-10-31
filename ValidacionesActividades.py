import sqlite3
from bd import Conexion


class ValidacionesActividades:
    @staticmethod
    def validacionNombre():
        nombre = input("Ingrese un nombre para la actividad:")
        while True:
            if nombre and nombre.strip().isalpha():
                return nombre.strip()
            else:
                print("Error: El nombre de la actividad no puede estar vacío y debe contener solo letras.")
                nombre = input("Por favor, ingrese el nombre nuevamente: ")