from base.bdd import get_connection
from models.entities.Profesional import Profesional

class ModProfesional:

  @classmethod
  def getProfesionales(self):
    try:
      cx = get_connection()
      profesionales = []
      with cx.cursor() as cursor:
        cursor.execute('SELECT rut_prof, p_nombre, s_nombre, ap_paterno, ap_materno, contraseña, direccion, celular, email , tarifa, estado, fecha_registro, id_especialidad  FROM profesional')
        resultset = cursor.fetchall()
        for row in resultset:
          profesional = Profesional(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])
          profesionales.append(profesional.to_JSON())
        cx.close()
        return profesionales
    except Exception as ex:
      raise Exception(ex)


  @classmethod
  def add_profesional(self, profesional):
    try:
      cx = get_connection()
      with cx.cursor() as cursor:
        cursor.execute("INSERT INTO profesional VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
          (profesional.rut_prof, profesional.p_nombre,
          profesional.s_nombre, profesional.ap_paterno, profesional.ap_materno, profesional.contraseña, profesional.direccion, profesional.celular,
          profesional.email, profesional.tarifa, profesional.estado, profesional.fecha_registro, profesional.id_especialidad)
        )
        affected_rows = cursor.rowcount
        cx.commit()
      cx.close()
      return affected_rows
    except Exception as ex:
      raise Exception(ex)