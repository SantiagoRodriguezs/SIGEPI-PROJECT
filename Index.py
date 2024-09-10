from flask import Flask, request, flash
import conexion, routes

app = Flask(__name__)
app.secret_key = 'LLAVE_SEGURA'  

#------- INICIAR CONEXION --------#
conexion.init_app(app)


#------- VALIDAR CONEXION --------#
@app.route('/test-db')
def test_db():
    message = conexion.test_connection()
    return message

#http://localhost:5000/test-db


#------- LOGIN LOGICA --------#
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        documento = request.form.get('NumDocUsu')
        contrasena = request.form.get('TelefonoUsu')
        db = conexion.get_db()

        try:
            query = "SELECT * FROM Usuario WHERE NumDocUsu = %s AND TelefonoUsu = %s"
            params = (documento, contrasena)

            with db.cursor() as cursor:
                print(f"Buscando usuario con NumDocUsu: {documento} y TelefonoUsu: {contrasena}")
                cursor.execute(query, params)
                usuario = cursor.fetchone()
                print(f"Resultado de la consulta: {usuario}")

            if usuario:
                rol = usuario['RolUsu']
                if rol == 1:
                    return routes.MenuAdmin()
                elif rol == 2:
                    return routes.MenuServicio()
                elif rol == 3:
                    return routes.MenuSupervisor()
                elif rol == 4:
                    return routes.MenuTransportador()
                elif rol == 5:
                    return routes.Mecanicos()
            else:
                flash('Número de documento o contraseña incorrectos.')
        except Exception as e:
            print(f'Error al conectar con la base de datos: {e}')
            flash(f'Error al conectar con la base de datos: {e}')
    return routes.Login()


#------- TRANSPORTADOR --------#

if __name__ == '__main__':
    app.run(debug=True)
