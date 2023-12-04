class Profesional():

  def __init__(self,
               rut_prof=None,
               p_nombre=None,
               s_nombre=None,
               ap_paterno=None,
               ap_materno=None,
               contraseña=None,
               direccion=None,
               celular=None,
               email=None,
               tarifa=None,
               estado=None,
               fecha_registro=None,
               id_especialidad=None):
    self.rut_prof = rut_prof
    self.p_nombre = p_nombre
    self.s_nombre = s_nombre
    self.ap_paterno = ap_paterno
    self.ap_materno = ap_materno
    self.contraseña = contraseña
    self.direccion = direccion
    self.celular = celular
    self.email = email
    self.tarifa = tarifa
    self.estado = estado
    self.fecha_registro = fecha_registro
    self.id_especialidad = id_especialidad

  def to_JSON(self):
    return {
        'rut_prof': self.rut_prof,
        'p_nombre': self.p_nombre,
        's_nombre': self.s_nombre,
        'ap_paterno': self.ap_paterno,
        'ap_materno': self.ap_materno,
        'contraseña': self.contraseña,
        'direccion': self.direccion,
        'celular': self.celular,
        'email': self.email,
        'tarifa': self.tarifa,
        'estado': self.estado,
        'fecha_registro': self.fecha_registro,
        'especialidad': self.id_especialidad
    }
