from base.bdd import get_connection
from models.entities.Paciente import Paciente
from flask import request

from itertools import cycle

class ModPaciente():

  @classmethod
  def getPacientes(self):
    try:
      cx = get_connection()
      pacientes = []
      with cx.cursor() as cursor:
        cursor.execute(
            'SELECT rut_pac, p_nombre, s_nombre, ap_paterno, ap_materno, contraseña, orden_apellido, fecha_nacimiento, direccion, celular, email, estado, nombre_social, fecha_registro, id_comuna, id_prevision FROM paciente'
        )
        resultset = cursor.fetchall()
        for row in resultset:
          paciente = Paciente(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15])
          pacientes.append(paciente.to_JSON())
        cx.close()
        return pacientes
    except Exception as ex:
      raise Exception(ex)

  
  @classmethod
  def add_paciente(self, paciente):
    try:
      cx = get_connection()
      with cx.cursor() as cursor:
        cursor.execute("INSERT INTO paciente VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
           (paciente.rut_pac, paciente.p_nombre, paciente.s_nombre, paciente.ap_paterno, paciente.ap_materno, paciente.contraseña, paciente.orden_apellido,
            paciente.fecha_nacimiento, paciente.direccion, paciente.celular, paciente.email, paciente.estado, paciente.nombre_social,
            paciente.fecha_registro, paciente.id_comuna, paciente.id_prevision)
            )
        affected_rows = cursor.rowcount
        cx.commit()
      cx.close()
      return affected_rows
    except Exception as ex:
      raise Exception(ex)


