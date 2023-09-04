class Curso:
    def __init__(self, fecha_comienzo, titulo, Descripcion, Objetivos, Programa, costo, Duracion, foto, estado, categoria):
        self.fecha_comienzo = fecha_comienzo
        self.titulo = titulo 
        self.descripcion = Descripcion
        self.Objetivos = Objetivos
        self.programa = Programa
        self.costo = costo
        self.Duracion = Duracion
        self.foto = foto
        self.estado = estado
        self.categoria = categoria
        self.clases = []

    
    def mostrar_informacion(self):
        print(f'Fecha_comienzo: {self.fecha_comienzo}')
        print(f'Titulo: {self.titulo}')
        print(f"Descripcion: {self.descripcion}")
        print(f"Objetivos: {self.Objetivos}")
        print(f"Programa: {self.programa}")
        print(f"Costo: {self.costo}")
        print(f"Duracion: {self.Duracion}")
        print(f"Foto: {self.foto}")        
        print(f"Estado: {self.estado}")
        print(f"Categoría: {self.categoria}")
        print("-" * 30)

# Crear instancias de cursos
curso1 = Curso("14/10/2023", 
               "Soldador Básico", 
               "Enseñar las habilidades esenciales necesarias para realizar trabajos de soldadura de manera segura y efectiva", 
               "Desarrollar Habilidades de Soldadura",
               "Se distribuye en varias clases que cubren los aspectos fundamentales de la soldadura",
               "15.000",
               "6 meses", 
               'Imagen',
               "disponible",
               'Basico')

curso2 = Curso("16/10/2023", 
               "Auxiliar en Costrucción", 
               "Trabajador que presta apoyo en diversas tareas y actividades dentro de un sitio de construcción", 
               "Proporcionar apoyo esencial en un sitio de construcción para garantizar que el trabajo se realice de manera eficiente y segura",
               "Formación completa que cubre desde conceptos básicos de construcción y seguridad hasta habilidades prácticas y ética profesional. Incluye PASANTÍA",
               "12.000",
               "6 meses", 
               'Imagen',
               "disponible",
               'Intermedio')
               
# Mostrar información de los cursos
curso1.mostrar_informacion()
curso2.mostrar_informacion()

class Clase:
    def __init__(self, fecha, titulo, contenido, url_drive):
        self.fecha = fecha
        self.titulo = titulo
        self.contenido = contenido
        self.url_drive = url_drive

class Docente:
    def __init__(self, apellido, nombre, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono, correo):
        self.apellido = apellido
        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono = telefono
        self.correo = correo
        self.cursos = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

               
    def mostrar_informacion(self):
        print(f'Apellido: {self.apellido}')
        print(f'Nombre: {self.nombre}')
        print(f"DNI: {self.dni}")
        print(f"Fecha de Nacimien:{self.fecha_nacimiento}")
        print(f"Dirección: {self.direccion}")
        print(f"Localidad: {self.localidad}")
        print(f"Código Postal: {self.codigo_postal}")
        print(f'Provincia: {self.provincia}')
        print(f'Teléfono: {self.telefono}')
        print(f'Correo: {self.correo}')
        print("-" * 30)
        
# Crear docentes: 
docente1 = Docente("López",
                   "Juan",
                   "12345678",
                   "1980-05-20",
                   "Calle 123",
                   "Sunchales",
                   "12345",
                   "Santa Fe",
                   "1234567890",
                   "juan@example.com")


docente2 = Docente("Gómez",
                   "María", 
                   "98765432",
                   "1975-02-15",
                   "Av. Principal", 
                   "San Pedro", 
                   "54321", 
                   "Córdoba", 
                   "9876543210", 
                   "maria@example.com")
        
# Mostrar información de los docentes: 
docente1.mostrar_informacion()
docente2.mostrar_informacion()

class UsuarioFinal:
    def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono, correo, clave_acceso, estado):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono = telefono
        self.correo = correo
        self.clave_acceso = clave_acceso
        self.estado = estado
        self.cursos_inscritos = []

    def inscribirse_a_curso(self, curso):
        self.cursos_inscritos.append(curso)
        
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')
        print(f'Apellido: {self.apellido}')
        print(f"DNI: {self.dni}")
        print(f"Dirección: {self.direccion}")
        print(f"Fecha de Nacimien:{self.fecha_nacimiento}")
        print(f"Localidad: {self.localidad}")
        print(f"Código Postal: {self.codigo_postal}")
        print(f'Provincia: {self.provincia}')
        print(f'Teléfono: {self.telefono}')
        print(f'Correo: {self.correo}')
        print (f'Clave de Acceso:{self.clave_acceso}')
        print(f'Estado: {self.estado}')
        print("-" * 30)
        
        
def crear_cuenta():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    direccion = input("Dirección: ")
    fecha_nacimiento = input("Fecha de Nacimiento: ")
    localidad = input("Localidad: ")
    codigo_postal = input("Código Postal: ")
    provincia = input("Provincia: ")
    telefono_celular = input("Teléfono Celular: ")
    email = input("Email: ")

    
    clave = input("Ingrese su clave de acceso: ")
    confirmar_clave = input("Confirme su clave de acceso: ")

    if clave != confirmar_clave:
        print("Las claves no coinciden.")
        return


    usuario = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "direccion": direccion,
        "fecha_nacimiento": fecha_nacimiento,
        "localidad": localidad,
        "codigo_postal": codigo_postal,
        "provincia": provincia,
        "telefono_celular": telefono_celular,
        "email": email,
        "clave": clave
    }

    print("Cuenta de usuario creada con éxito.")


crear_cuenta()