import os
from models.estudiante import Estudiante

class EstudianteDAO:
    def __init__(self, nombre_archivo="estudiantes.txt"):
        self.nombre_archivo = nombre_archivo
        self.ruta_archivo = os.path.join(os.getcwd(), self.nombre_archivo)
    
    def guardar_estudiante(self, estudiante):
        """Guarda un estudiante en el archivo"""
        try:
            with open(self.ruta_archivo, 'a', encoding='utf-8') as archivo:
                archivo.write(estudiante.to_string() + '\n')
            return True
        except Exception as e:
            print(f"Error al guardar estudiante: {e}")
            return False
    
    def cargar_estudiantes(self):
        """Carga todos los estudiantes del archivo"""
        estudiantes = []
        try:
            if os.path.exists(self.ruta_archivo):
                with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                    for linea in archivo:
                        estudiante = Estudiante.from_string(linea)
                        if estudiante:
                            estudiantes.append(estudiante)
            return estudiantes
        except Exception as e:
            print(f"Error al cargar estudiantes: {e}")
            return []
    
    def buscar_por_cif(self, cif):
        """Busca un estudiante por su CIF"""
        estudiantes = self.cargar_estudiantes()
        for estudiante in estudiantes:
            if estudiante.cif == cif:
                return estudiante
        return None
    
    def actualizar_estudiante(self, cif, estudiante_actualizado):
        """Actualiza los datos de un estudiante"""
        estudiantes = self.cargar_estudiantes()
        encontrado = False
        
        for i, estudiante in enumerate(estudiantes):
            if estudiante.cif == cif:
                estudiantes[i] = estudiante_actualizado
                encontrado = True
                break
        
        if encontrado:
            return self._guardar_todos_estudiantes(estudiantes)
        return False
    
    def eliminar_estudiante(self, cif):
        """Elimina un estudiante por su CIF"""
        estudiantes = self.cargar_estudiantes()
        estudiantes_filtrados = [est for est in estudiantes if est.cif != cif]
        
        if len(estudiantes_filtrados) < len(estudiantes):
            return self._guardar_todos_estudiantes(estudiantes_filtrados)
        return False
    
    def _guardar_todos_estudiantes(self, estudiantes):
        """Guarda todos los estudiantes en el archivo (sobrescribe)"""
        try:
            with open(self.ruta_archivo, 'w', encoding='utf-8') as archivo:
                for estudiante in estudiantes:
                    archivo.write(estudiante.to_string() + '\n')
            return True
        except Exception as e:
            print(f"Error al guardar estudiantes: {e}")
            return False
    
    def obtener_estadisticas(self):
        """Obtiene estadísticas de aprobados y reprobados"""
        estudiantes = self.cargar_estudiantes()
        total = len(estudiantes)
        aprobados = len([est for est in estudiantes if est.estado == "APROBADO"])
        reprobados = total - aprobados
        
        return {
            'total': total,
            'aprobados': aprobados,
            'reprobados': reprobados,
            'porcentaje_aprobados': (aprobados / total * 100) if total > 0 else 0,
            'porcentaje_reprobados': (reprobados / total * 100) if total > 0 else 0
        }
    
    def obtener_por_grupo(self, asignatura):
        """Obtiene estudiantes por asignatura/grupo"""
        estudiantes = self.cargar_estudiantes()
        return [est for est in estudiantes if est.asignatura.lower() == asignatura.lower()]

