# Sistema de Registro de Notas de Estudiantes

## Descripción
Aplicación modular en Python para registrar y gestionar las notas de estudiantes por grupo.

## Estructura del Proyecto
```
IntroProg-G2-S13/
├── models/
│   ├── __init__.py
│   └── estudiante.py        # Modelo de datos del estudiante
├── dao/
│   ├── __init__.py
│   └── estudiante_dao.py    # Acceso a datos (archivo de texto)
├── utils/
│   ├── __init__.py
│   └── validaciones.py      # Funciones de validación
├── main.py                 # Script principal
├── estudiantes.txt         # Archivo de datos (se crea automáticamente)
└── README.md
```

## Funcionalidades
1. **Registrar estudiante**: Captura CIF, nombres, apellidos, carrera, asignatura y 3 notas
2. **Mostrar estudiantes**: Lista todos los estudiantes registrados
3. **Actualizar estudiante**: Modifica los datos de un estudiante existente
4. **Eliminar estudiante**: Elimina un estudiante por CIF
5. **Ver estadísticas**: Muestra aprobados, reprobados y porcentajes

## Datos del Estudiante
- **CIF**: Código de identificación del estudiante
- **Nombres**: Nombres del estudiante
- **Apellidos**: Apellidos del estudiante
- **Carrera**: Carrera que estudia
- **Asignatura**: Materia/grupo
- **Notas**: 3 notas con base 100
- **Nota Final**: Promedio de las 3 notas
- **Estado**: APROBADO (>= 70) o REPROBADO (< 70)

## Cómo ejecutar
```bash
python main.py
```

## Validaciones
- CIF: Mínimo 5 caracteres
- Nombres/Apellidos: Mínimo 2 caracteres
- Notas: Entre 0 y 100
- Todos los campos son obligatorios

## Almacenamiento
Los datos se guardan en un archivo de texto llamado `estudiantes.txt` en el formato:
```
CIF|Nombres|Apellidos|Carrera|Asignatura|Nota1|Nota2|Nota3|NotaFinal|Estado
```

## Arquitectura
- **Modelos**: Clases que representan los datos
- **DAO**: Manejo de persistencia de datos
- **Utils**: Funciones auxiliares y validaciones
- **Main**: Interfaz de usuario y lógica principal

