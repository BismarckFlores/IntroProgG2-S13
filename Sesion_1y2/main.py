import sys
from dao import EstudianteDAO
from models import Estudiante
from utils import *

def mostrar_menu():
    print("1. Registrar nuevo estudiante")
    print("2. Mostrar estudiantes")
    print("3. Actualizar estudiante")
    print("4. Eliminar estudiante")
    print("5. Ver estadísticas")
    print("6. Salir")

def registrar_estudiante(dao):
    cif = solicitar_entrada("Ingrese el CIF: ")
    nombres = solicitar_entrada("Ingrese los nombres: ")
    apellidos = solicitar_entrada("Ingrese los apellidos: ")
    carrera = solicitar_entrada("Ingrese la carrera: ")
    asignatura = solicitar_entrada("Ingrese la asignatura: ")
    nota1 = solicitar_nota("Ingrese Nota 1: ")
    nota2 = solicitar_nota("Ingrese Nota 2: ")
    nota3 = solicitar_nota("Ingrese Nota 3: ")
    estudiante = Estudiante(cif, nombres, apellidos, carrera, asignatura, nota1, nota2, nota3)

    errores = validar_datos_estudiante(cif, nombres, apellidos, carrera, asignatura)
    errores_notas = validar_notas(nota1, nota2, nota3)

    if errores or errores_notas:
        print("Errores en los datos:")
        for error in errores + errores_notas:
            print("-", error)
        return

    if dao.guardar_estudiante(estudiante):
        print("Estudiante guardado correctamente.")
    else:
        print("Error guardando el estudiante.")

def mostrar_estudiantes(dao):
    estudiantes = dao.cargar_estudiantes()
    for estudiante in estudiantes:
        print(estudiante)

def actualizar_estudiante(dao):
    cif = solicitar_entrada("Ingrese el CIF del estudiante a actualizar: ")
    estudiante = dao.buscar_por_cif(cif)
    if estudiante:
        nombres = solicitar_entrada("Ingrese los nuevos nombres: ")
        apellidos = solicitar_entrada("Ingrese los nuevos apellidos: ")
        carrera = solicitar_entrada("Ingrese la nueva carrera: ")
        asignatura = solicitar_entrada("Ingrese la nueva asignatura: ")
        nota1 = solicitar_nota("Ingrese Nota 1: ")
        nota2 = solicitar_nota("Ingrese Nota 2: ")
        nota3 = solicitar_nota("Ingrese Nota 3: ")
        estudiante_actualizado = Estudiante(cif, nombres, apellidos, carrera, asignatura, nota1, nota2, nota3)
        if dao.actualizar_estudiante(cif, estudiante_actualizado):
            print("Estudiante actualizado correctamente.")
        else:
            print("Error actualizando el estudiante.")
    else:
        print("Estudiante no encontrado.")

def eliminar_estudiante(dao):
    cif = solicitar_entrada("Ingrese el CIF del estudiante a eliminar: ")
    if dao.eliminar_estudiante(cif):
        print("Estudiante eliminado correctamente.")
    else:
        print("Error eliminando el estudiante o estudiante no encontrado.")

def ver_estadisticas(dao):
    estadisticas = dao.obtener_estadisticas()
    print("Total Estudiantes: ", estadisticas['total'])
    print("Aprobados: ", estadisticas['aprobados'])
    print("Reprobados: ", estadisticas['reprobados'])
    print("% Aprobados: ", estadisticas['porcentaje_aprobados'])
    print("% Reprobados: ", estadisticas['porcentaje_reprobados'])

def main():
    dao = EstudianteDAO()
    while True:
        mostrar_menu()
        opcion = solicitar_entrada("Seleccione una opción: ")
        if opcion == "1":
            registrar_estudiante(dao)
        elif opcion == "2":
            mostrar_estudiantes(dao)
        elif opcion == "3":
            actualizar_estudiante(dao)
        elif opcion == "4":
            eliminar_estudiante(dao)
        elif opcion == "5":
            ver_estadisticas(dao)
        elif opcion == "6":
            print("Saliendo...")
            sys.exit(0)
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

