# ============================================================
# Classwork #10 - School Management System
# ============================================================

# ---- INPUT: Data structures ----

usuarios = {
    'lbenitez': {'password': '1234', 'rol': 'alumno',       'nombre': 'Luis Benítez'},
    'mcastro':  {'password': '1234', 'rol': 'alumno',       'nombre': 'Mariana Castro'},
    'dhierro':  {'password': '1234', 'rol': 'alumno',       'nombre': 'Diego Hierro'},
    'sorozco':  {'password': '1234', 'rol': 'alumno',       'nombre': 'Sofía Orozco'},
    'ajimenez': {'password': '1234', 'rol': 'alumno',       'nombre': 'Alejandro Jiménez'},
    'vnavarro': {'password': '1234', 'rol': 'alumno',       'nombre': 'Valeria Navarro'},
    'fherrera': {'password': '1234', 'rol': 'maestro',      'nombre': 'Fernando Herrera'},
    'gmedina':  {'password': '1234', 'rol': 'coordinador',  'nombre': 'Gabriela Medina'},
}

# PROCESS: materias is a tuple because subjects never change during execution
materias = ('Matemáticas', 'Programación', 'Inglés')

calificaciones = {
    'lbenitez': {'Matemáticas': 8.5, 'Programación': 9.0, 'Inglés': 7.5},
    'mcastro':  {'Matemáticas': 9.0, 'Programación': 8.0, 'Inglés': 8.5},
    'dhierro':  {'Matemáticas': 7.0, 'Programación': 8.5, 'Inglés': 6.5},
    'sorozco':  {'Matemáticas': 9.5, 'Programación': 9.0, 'Inglés': 9.0},
    'ajimenez': {'Matemáticas': 6.5, 'Programación': 7.5, 'Inglés': 8.0},
    'vnavarro': {'Matemáticas': 8.0, 'Programación': 8.0, 'Inglés': 7.0},
}


# ---- FUNCTIONS ----

def confirmar_cambio(alumno_nombre, materia, cal_antigua, cal_nueva):
    """
    Pregunta al profesor si está seguro de modificar la calificación.
    Devuelve True si acepta el cambio, False en caso contrario.
    """
    print(f'\n[CONFIRMACIÓN] ¿Está seguro de cambiar la calificación de {alumno_nombre} en {materia}?')
    print(f'  Calificación actual: {cal_antigua}')
    print(f'  Nueva calificación:  {cal_nueva}')
    
    while True:
        respuesta = input('\n¿Proceder con el cambio? (s/n): ').strip().lower()
        if respuesta in ('s', 'si', 'sí'):
            return True
        elif respuesta in ('n', 'no'):
            return False
        else:
            print('  Opción no válida. Por favor ingresa "s" para sí o "n" para no.')


# ============================================================
# PROCESS: Login loop — keeps asking until credentials match
# ============================================================

logged_in = False
usuario_actual = ''

while not logged_in:
    # INPUT: ask for credentials
    usuario_input = input('Usuario: ')
    password_input = input('Contraseña: ')

    # PROCESS: validate username exists and password matches
    if usuario_input in usuarios and usuarios[usuario_input]['password'] == password_input:
        logged_in = True
        usuario_actual = usuario_input
    else:
        # OUTPUT: wrong credentials message
        print('Usuario o contraseña incorrectos. Intenta de nuevo.\n')

# OUTPUT: welcome message after successful login
rol_actual = usuarios[usuario_actual]['rol']
nombre_actual = usuarios[usuario_actual]['nombre']
print(f'\nBienvenido, {nombre_actual} ({rol_actual})\n')

# ============================================================
# PROCESS: Branch by role
# ============================================================

if rol_actual == 'alumno':

    # ----------------------------------------------------------
    # STUDENT MENU
    # ----------------------------------------------------------

    # OUTPUT: grade report header
    print(f'Boleta de {nombre_actual}')
    print('-' * 30)

    # PROCESS: build approved/pending sets while printing grades
    aprobadas = set()

    for materia in materias:
        # INPUT: grade stored in calificaciones
        calificacion = calificaciones[usuario_actual][materia]
        # OUTPUT: one subject per line
        print(f'{materia}: {calificacion}')
        # PROCESS: classify subject
        if calificacion >= 7.0:
            aprobadas.add(materia)

    # PROCESS: set difference gives pending subjects
    pendientes = set(materias) - aprobadas

    # OUTPUT: approved and pending sets
    print(f'\nMaterias aprobadas:  {aprobadas}')
    print(f'Materias pendientes: {pendientes}')

elif rol_actual == 'maestro':

    # ----------------------------------------------------------
    # TEACHER MENU
    # ----------------------------------------------------------

    # OUTPUT: list of students
    print('Lista de alumnos:')
    print('-' * 30)
    for user, datos in usuarios.items():
        if datos['rol'] == 'alumno':
            print(f'  {user} — {datos["nombre"]}')

    print()

    # INPUT: teacher selects a student
    alumno_sel = ''
    while alumno_sel not in calificaciones:
        alumno_sel = input('Alumno (usuario): ')
        if alumno_sel not in calificaciones:
            print('  Usuario no encontrado. Intenta de nuevo.')

    # INPUT: teacher selects a subject (must be in materias tuple)
    materia_sel = ''
    while materia_sel not in materias:
        materia_sel = input(f'Materia {materias}: ')
        if materia_sel not in materias:
            print('  Materia no válida. Intenta de nuevo.')

    # INPUT: new grade value
    nueva_cal = -1.0
    while not (0.0 <= nueva_cal <= 10.0):
        try:
            nueva_cal = float(input('Nueva calificación (0.0 - 10.0): '))
            if not (0.0 <= nueva_cal <= 10.0):
                print('  La calificación debe estar entre 0.0 y 10.0.')
        except ValueError:
            print('  Por favor ingresa un número válido.')
            nueva_cal = -1.0

    # PROCESS: Get old grade and ask for confirmation before overwriting
    cal_antigua = calificaciones[alumno_sel][materia_sel]
    alumno_nombre_sel = usuarios[alumno_sel]['nombre']
    
    if confirmar_cambio(alumno_nombre_sel, materia_sel, cal_antigua, nueva_cal):
        # PROCESS: overwrite grade in calificaciones
        calificaciones[alumno_sel][materia_sel] = nueva_cal
        # OUTPUT: confirmation
        print(f'\nCalificación actualizada con éxito.')
        print(f'  Alumno:   {alumno_nombre_sel}')
        print(f'  Materia:  {materia_sel}')
        print(f'  Nueva calificación: {nueva_cal}')
    else:
        # OUTPUT: cancellation message
        print('\nCambio cancelado. La calificación original se mantiene intacta.')

elif rol_actual == 'coordinador':

    # ----------------------------------------------------------
    # COORDINATOR MENU (read-only)
    # ----------------------------------------------------------

    # OUTPUT 1: list of teachers
    print('=== Maestros ===')
    for user, datos in usuarios.items():
        if datos['rol'] == 'maestro':
            print(f'  {user} — {datos["nombre"]}')

    # OUTPUT 2: list of subjects from the tuple
    print('\n=== Materias ===')
    for materia in materias:
        print(f'  {materia}')

    # OUTPUT 3: full grade report per student
    print('\n=== Alumnos y Calificaciones ===')
    for alumno, grades in calificaciones.items():
        nombre_alumno = usuarios[alumno]['nombre']
        print(f'\n  {nombre_alumno} ({alumno}):')
        for materia in materias:
            print(f'    {materia}: {grades[materia]}')

else:
    # OUTPUT: unknown role guard
    print('Rol no reconocido. Contacta al administrador.')