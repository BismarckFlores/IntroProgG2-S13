def validar_cif(cif):
    """Valida que el CIF no esté vacío y tenga formato válido"""
    if not cif or not cif.strip():
        return False
    return len(cif.strip()) >= 5  # Mínimo 5 caracteres

def validar_nombre(nombre):
    """Valida que el nombre no esté vacío"""
    if not nombre or not nombre.strip():
        return False
    return len(nombre.strip()) >= 2  # Mínimo 2 caracteres

def validar_nota(nota):
    """Valida que la nota esté entre 0 y 100"""
    try:
        nota_float = float(nota)
        return 0 <= nota_float <= 100
    except (ValueError, TypeError):
        return False

def validar_datos_estudiante(cif, nombres, apellidos, carrera, asignatura):
    """Valida todos los datos básicos del estudiante"""
    errores = []
    
    if not validar_cif(cif):
        errores.append("CIF debe tener al menos 5 caracteres")
    
    if not validar_nombre(nombres):
        errores.append("Nombres debe tener al menos 2 caracteres")
    
    if not validar_nombre(apellidos):
        errores.append("Apellidos debe tener al menos 2 caracteres")
    
    if not validar_nombre(carrera):
        errores.append("Carrera debe tener al menos 2 caracteres")
    
    if not validar_nombre(asignatura):
        errores.append("Asignatura debe tener al menos 2 caracteres")
    
    return errores

def validar_notas(nota1, nota2, nota3):
    """Valida las tres notas"""
    errores = []
    
    if not validar_nota(nota1):
        errores.append("Nota 1 debe estar entre 0 y 100")
    
    if not validar_nota(nota2):
        errores.append("Nota 2 debe estar entre 0 y 100")
    
    if not validar_nota(nota3):
        errores.append("Nota 3 debe estar entre 0 y 100")
    
    return errores

def solicitar_entrada(mensaje, validador=None):
    """Solicita entrada del usuario con validación opcional"""
    while True:
        entrada = input(mensaje).strip()
        if validador:
            if validador(entrada):
                return entrada
            else:
                print("Entrada inválida. Intente nuevamente.")
        else:
            if entrada:  # Solo verificar que no esté vacío
                return entrada
            else:
                print("Este campo no puede estar vacío.")

def solicitar_nota(mensaje):
    """Solicita una nota con validación"""
    while True:
        try:
            nota = float(input(mensaje))
            if validar_nota(nota):
                return nota
            else:
                print("La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Por favor ingrese un número válido.")

