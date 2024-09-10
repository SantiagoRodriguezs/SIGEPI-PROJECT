from flask import Flask, render_template

app = Flask(__name__)

#------- GENERALES --------#
@app.route('/Login')
def Login():
    return render_template('Index.html')

@app.route('/Menu')
def Menu():
    return render_template('Vistas.html')

#------- ADMINISTRADOR --------#
@app.route('/MenuAdmin')
def MenuAdmin():
    return render_template('PrincipalAdmin.html')

@app.route('/AgregarUsuarios')
def AgregarUsuarios():
    return render_template('AgUsuarios.html')

@app.route('/AgregarTrailers')
def AgregarTrailers():
    return render_template('AgTrailers.html')

@app.route('/AgregarVehiculos')
def AgregarVehiculos():
    return render_template('AgVehiculos.html')

@app.route('/ListadoUsuarios')
def ListadoUsuarios():
    return render_template('ListUsuarios.html')

@app.route('/PerfilAdministrador')
def PerfilAdministrador():
    return render_template('Perfil.html')

@app.route('/EditarPerfilAdministrador')
def EditarPerfilAdministrador():
    return render_template('EditPerfilAd.html')


#------- MECANICOS --------#
@app.route('/Mecanicos')
def Mecanicos():
    return render_template('Mecanicos.html')


#------- SERVICIO AL CLIENTE --------#
@app.route('/MenuServicio')
def MenuServicio():
    return render_template('PrincipalServicio.html')

@app.route('/GestionarPedidos')
def GestionarPedidos():
    return render_template('GestPedidos.html')

@app.route('/RegistrarPedido')
def RegistrarPedido():
    return render_template('RegisPedidos.html')

@app.route('/EditarPedido')
def EditarPedido():
    return render_template('EditPedidos.html')


#------- SUPERVISOR --------#
@app.route('/MenuSupervisor')
def MenuSupervisor():
    return render_template('PrincipalSupervisor.html')

@app.route('/ListadoFlotas')
def ListadoFlotas():
    return render_template('ListFlotas.html')

@app.route('/ConsultarRutaSupervisor')
def ConsultarRutaSupervisor():
    return render_template('ConsulRutaSup.html')

@app.route('/HistorialSupervisor')
def HistorialSupervisor():
    return render_template('HistorialSup.html')

@app.route('/ListadoPedidos')
def ListadoPedidos():
    return render_template('PedidosSup.html')

@app.route('/ProgramarItinerario')
def ProgramarItinerario():
    return render_template('ProgramarItinerario.html')

@app.route('/ConsultarItinerarios')
def ConsultarItinerarios():
    return render_template('ConsultarItinerario.html')

@app.route('/ReporteItinerario')
def ReporteItinerario():
    return render_template('ReporteSup.html')

@app.route('/PerfilSupervisor')
def PerfilSupervisor():
    return render_template('PerfilSup.html')

@app.route('/EditarPerfilSupervisor')
def EditarPerfilSupervisor():
    return render_template('EditPerfilSup.html')


#------- TRANSPORTADOR --------#
@app.route('/MenuTransportador')
def MenuTransportador():
    return render_template('PrincipalTransp.html')

@app.route('/ConsulItinerarioTransp')
def ConsulItinerarioTransp():
    return render_template('ConsultarTransp.html')

@app.route('/ReporteTransp')
def ReporteTransp():
    return render_template('ReporteTransp.html')

@app.route('/HistorialTransp')
def HistorialTransp():
    return render_template('HistorialTransp.html')

@app.route('/PerfilTransp')
def PerfilTransp():
    return render_template('PerfilTransp.html')

@app.route('/EditPerfilTransp')
def EditPerfilTransp():
    return render_template('EditPerfilTransp.html')