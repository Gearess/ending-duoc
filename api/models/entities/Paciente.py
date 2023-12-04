class Paciente():

  def __init__(self,
               rut_pac=None,
               p_nombre=None,
               s_nombre=None,
               ap_paterno=None,
               ap_materno=None,
               contraseña=None,
               orden_apellido=None,
               fecha_nacimiento=None,
               direccion=None,
               celular=None,
               email=None,
               estado=None,
               nombre_social=None,
               fecha_registro=None,
               id_comuna=None,
               id_prevision=None,):
    self.rut_pac = rut_pac
    self.p_nombre = p_nombre
    self.s_nombre = s_nombre
    self.ap_paterno = ap_paterno
    self.ap_materno = ap_materno
    self.contraseña = contraseña
    self.orden_apellido = orden_apellido
    self.fecha_nacimiento = fecha_nacimiento
    self.direccion = direccion
    self.celular = celular
    self.email = email
    self.estado = estado
    self.nombre_social = nombre_social
    self.fecha_registro = fecha_registro
    self.id_comuna = id_comuna
    self.id_prevision = id_prevision

  def to_JSON(self):
    return {
        'rut_pac': self.rut_pac,
        'p_nombre': self.p_nombre,
        's_nombre': self.s_nombre,
        'ap_paterno': self.ap_paterno,
        'ap_materno': self.ap_materno,
        'contraseña': self.contraseña,
        'orden_apellido': self.orden_apellido,
        'fecha_nacimiento': self.fecha_nacimiento,
        'direccion': self.direccion,
        'celular': self.celular,
        'email': self.email,
        'estado': self.estado,
        'nombre_social': self.nombre_social,
        'fecha_registro': self.fecha_registro,
        'comuna': self.id_comuna,
        'prevision': self.id_prevision
    }
