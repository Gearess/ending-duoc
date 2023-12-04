from flask import Blueprint, jsonify, request

from models.ModPaciente import ModPaciente

from models.entities.Paciente import Paciente  

main = Blueprint("paciente_blueprint", __name__)


@main.route("/")
def getPacientes():
  try:
    pacientes = ModPaciente.getPacientes()
    return jsonify(pacientes)
  except Exception as ex:
    return jsonify({"msg": str(ex)}), 500


@main.route("/add", methods=['POST'])
def add_paciente():
  try:
    paciente = Paciente(
    rut_pac = request.json['rut_pac'],
    p_nombre = request.json['p_nombre'],
    s_nombre = request.json['s_nombre'],
    ap_paterno = request.json['ap_paterno'],
    ap_materno = request.json['ap_materno'],
    contraseña = request.json['contraseña'],
    orden_apellido = request.json['orden_apellido'],
    fecha_nacimiento = request.json['fecha_nacimiento'],
    direccion = request.json['direccion'],
    celular = request.json['celular'],
    email = request.json['email'],
    estado = request.json['estado'],
    nombre_social = request.json['nombre_social'],
    fecha_registro = request.json['fecha_registro'],
    id_comuna = request.json['id_comuna'],
    id_prevision = request.json['id_prevision'])

    if ModPaciente.add_paciente(paciente):
      return jsonify({"message": "Paciente añadido"})
    else:
      return jsonify({"message": "Error"}), 500

    
    
  except Exception as ex:
    return jsonify({"message": str(ex)}), 500
  