class Estudiante:
    def __init__(self, cif, nombres, apellidos, carrera, asignatura, nota1=0, nota2=0, nota3=0):
        self.cif = cif
        self.nombres = nombres
        self.apellidos = apellidos
        self.carrera = carrera
        self.asignatura = asignatura
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota_final = self.calcular_nota_final()
        self.estado = self.determinar_estado()
    
    def calcular_nota_final(self):
        """Calcula el promedio de las 3 notas"""
        return (self.nota1 + self.nota2 + self.nota3) / 3
    
    def determinar_estado(self):
        """Determina si el estudiante aprobó o reprobó"""
        return "APROBADO" if self.nota_final >= 70 else "REPROBADO"
    
    def actualizar_notas(self, nota1, nota2, nota3):
        """Actualiza las notas del estudiante"""
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota_final = self.calcular_nota_final()
        self.estado = self.determinar_estado()
    
    def to_string(self):
        """Convierte el objeto a string para guardar en archivo"""
        return f"{self.cif}|{self.nombres}|{self.apellidos}|{self.carrera}|{self.asignatura}|{self.nota1}|{self.nota2}|{self.nota3}|{self.nota_final:.2f}|{self.estado}"
    
    @staticmethod
    def from_string(linea):
        """Crea un objeto Estudiante desde una línea de texto"""
        datos = linea.strip().split('|')
        if len(datos) >= 10:
            estudiante = Estudiante(
                cif=datos[0],
                nombres=datos[1],
                apellidos=datos[2],
                carrera=datos[3],
                asignatura=datos[4],
                nota1=float(datos[5]),
                nota2=float(datos[6]),
                nota3=float(datos[7])
            )
            return estudiante
        return None
    
    def __str__(self):
        return f"CIF: {self.cif} - {self.nombres} {self.apellidos} - {self.carrera} - {self.asignatura} - Nota Final: {self.nota_final:.2f} - {self.estado}"

