from enum import Enum
import datetime

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

class Usuario:
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, telefono, correo, direccion, localidad,  provincia, codigo_postal, estado, rol):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.localidad = localidad
        self.provincia = provincia
        self.codigo_postal = codigo_postal
        self.estado = estado
        self.rol = rol
        self.cursos_inscritos = []
        
class Docente(Usuario):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, telefono, correo, direccion, localidad,  provincia, codigo_postal):
        super(). __init__(nombre, apellido, dni, fecha_nacimiento, telefono, correo, direccion, localidad,  provincia, codigo_postal)


class UsuarioFinal:
    def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono, correo, clave_acceso, estado, rol, carrito_de_compra):
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
        self.rol = rol
        self.carrito_de_compra = carrito_de_compra
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
        print(f'rol:{self.rol}')
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
    rol = input ('rol:')

    
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
        "clave": clave,
        "rol": rol
    }

    print("Cuenta de usuario creada con éxito.")


crear_cuenta()

class incripcion_curso:
    def __init__(self, foto, titulo, duracion, costo):
        self.foto = foto
        self.titulo = titulo
        self.duracion = duracion
        self.costo = costo

def confirmar_compra(self):
    if not self.carrito_de_compras:
        print("El carrito de compras está vacío.")
        return

    # Calcula el monto total
    monto_total = sum(curso.costo for curso in self.carrito_de_compras)

    # Solicita al usuario seleccionar el medio de pago
    medio_de_pago = input("Seleccione el medio de pago (Tarjeta/Transferencia): ").lower()

    if medio_de_pago == "tarjeta":
        # Recopila los datos de la tarjeta de crédito/débito
        tarjeta_numero = input("Número de tarjeta: ")
        tarjeta_nombre = input("Nombre en la tarjeta: ")
        tarjeta_fecha_vencimiento = input("Fecha de vencimiento (MM/AA): ")
        tarjeta_cvv = input("CVV: ")

        # Registra la fecha de compra, usuario y monto total
        fecha_compra = datetime.date.today()
        compra = {
            "fecha_compra": fecha_compra,
            "usuario": f"{self.nombre} {self.apellido}",
            "monto_total": monto_total,
        }

        # Puedes guardar la información de la compra en una lista, base de datos, o donde lo necesites.
        print("Compra confirmada con éxito.")
        print("Resumen de la compra:")
        print(f"Fecha de compra: {fecha_compra}")
        print(f"Usuario: {self.nombre} {self.apellido}")
        print(f"Monto total: {monto_total}")
        print("Medio de pago: Tarjeta de crédito/débito")
        print("-" * 30)

    elif medio_de_pago == "transferencia":
        # Recopila los datos de la transferencia bancaria
        banco_destino = input("Banco de destino: ")
        numero_cuenta_destino = input("Número de cuenta de destino: ")

        # Registra la fecha de compra, usuario y monto total
        fecha_compra = datetime.date.today()
        compra = {
            "fecha_compra": fecha_compra,
            "usuario": f"{self.nombre} {self.apellido}",
            "monto_total": monto_total,
        }

        # Puedes guardar la información de la compra en una lista, base de datos, o donde lo necesites.
        print("Compra confirmada con éxito.")
        print("Resumen de la compra:")
        print(f"Fecha de compra: {fecha_compra}")
        print(f"Usuario: {self.nombre} {self.apellido}")
        print(f"Monto total: {monto_total}")
        print(f"Medio de pago: Transferencia bancaria a {banco_destino}, Número de cuenta: {numero_cuenta_destino}")
        print("-" * 30)

    else:
        print("Medio de pago no válido. Seleccione 'Tarjeta' o 'Transferencia'.")

# Agrega este método a la clase UsuarioFinal
UsuarioFinal.confirmar_compra = confirmar_compra

class Compra: 
    def __init__ (self, Id_Compra, Id_Carrito_Compra, Id_Medios_Pago, Id_Usuario, Fecha, Monto_Total):
        self.Id_Compra = Id_Compra
        self. Id_Carrito_compra = Id_Carrito_Compra
        self. Id_Medios_Pago = Id_Medios_Pago
        self. Id_Usuario = Id_Usuario
        self.Fecha = Fecha
        self.Monto_Total = Monto_Total
        
class Medios_de_Contacto:
    def __init__ (self, Id_MedioContacto, Fecha, Email, Telefono, Direccion, Nombre):
        self.Id_MedioContacto = Id_MedioContacto
        self.Fecha = Fecha
        self.Email = Email
        self.telefono = Telefono
        self.Direccion = Direccion
        self.Nombre = Nombre
               
class Tipos_Medio_Contacto(Medios_de_Contacto, Enum):
    WHATSAPP = (1, None, None, None, None, None)
    CORREO_ELECTRONICO = (2, None, None, None, None, None)
    CALL_CENTER = (3, None, None, None, None, None)
    REFERIDO_INTERNO = (4, None, None, None, None, None)

    def __init__(self, Id_MedioContacto, Fecha, Email, Telefono, Direccion, Nombre):
        self.Id_MedioContacto = Id_MedioContacto
        self.Fecha = Fecha
        self.Email = Email
        self.Telefono = Telefono
        self.Direccion = Direccion
        self.Nombre = Nombre

# Ejemplo de uso:
whatsapp = Tipos_Medio_Contacto.WHATSAPP
whatsapp.Fecha = "2023-09-18"
whatsapp.Email = "ejemplo@gmail.com"
whatsapp.Telefono = "123456789"
whatsapp.Direccion = "Calle Principal"
whatsapp.Nombre = "Juan"

print("Tipo de Medio de Contacto:", whatsapp)
print("ID:", whatsapp.Id_MedioContacto)
print("Fecha:", whatsapp.Fecha)
print("Email:", whatsapp.Email)
print("Teléfono:", whatsapp.Telefono)
print("Dirección:", whatsapp.Direccion)
print("Nombre:", whatsapp.Nombre)