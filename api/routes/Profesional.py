from flask import Blueprint, jsonify, request

from models.ModProfesional import ModProfesional

from models.entities.Profesional import Profesional

main = Blueprint("profesional_blueprint", __name__)

@main.route("/")
def getProfesionales():
  try:
    profesionales = ModProfesional.getProfesionales()
    return jsonify(profesionales)
  except Exception as ex:
    return jsonify({"msg": str(ex)}), 500

@main.route("/add", methods=['POST'])
def add_profesional():
  try:
    profesional = Profesional(rut_prof=request.json['rut_prof'],
                    p_nombre=request.json['p_nombre'],
                    s_nombre=request.json['s_nombre'],
                    ap_paterno=request.json['ap_paterno'],
                    ap_materno=request.json['ap_materno'],
                    contraseña=request.json['contraseña'],
                    direccion=request.json['direccion'],
                    celular=request.json['celular'],
                    email=request.json['email'],
                    tarifa=request.json['tarifa'],
                    estado=request.json['estado'],
                    fecha_registro=request.json['fecha_registro'],
                    id_especialidad=request.json['id_especialidad'])
    if ModProfesional.add_profesional(profesional):
      return jsonify({"message": "Medico añadido"})
    else:
      return jsonify({"message": "Error"}), 500
  except Exception as ex:
    print("hola")
    return jsonify({"message": str(ex)}), 500
