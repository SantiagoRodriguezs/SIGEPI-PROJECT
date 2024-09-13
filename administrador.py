from datetime import datetime
import conexion

class Administrador:
    def __init__(self, rol='', nombre='', apellidos='', fecha_nac='', num_doc='', correo='', telefono='', direccion='', estado=''):
        self.rol = rol
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nac = fecha_nac
        self.num_doc = num_doc
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.estado = estado

    def agregar_usuario(self):
        db = conexion.get_db()
        fecha_registro = datetime.now().date()
        try:
            query = """
            CALL InsUsuarios(%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            params = (
                self.rol,
                self.num_doc,
                self.fecha_nac,
                self.nombre,
                fecha_registro,
                self.correo,
                self.telefono,
                self.direccion,
                self.estado
            )
            with db.cursor() as cursor:
                cursor.execute(query, params)
                db.commit()
                print(f"Usuario {self.nombre} agregado correctamente.")
        except Exception as e:
            print(f'Error al agregar usuario: {e}')
            db.rollback()


    def obtener_info_usuarios(self):
        bd = conexion.get_db()
        try:
            query = "SELECT * FROM infoUsuAdministrador;"
            with bd.cursor() as cursor:
                cursor.execute(query)
                usuarios = cursor.fetchall()
                
                return usuarios
        except Exception as e:
            print(f'Error al obtener información de usuarios: {e}')
            return []
