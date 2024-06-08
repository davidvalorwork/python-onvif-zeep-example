import math

"""
Calcula el ángulo de rotación horizontal entre dos coordenadas GPS.

Args:
  lat_origen: Latitud del punto de origen (en grados).
  lon_origen: Longitud del punto de origen (en grados).
  lat_1: Latitud de la primera coordenada (en grados).
  lon_1: Longitud de la primera coordenada (en grados).
  lat_2: Latitud de la segunda coordenada (en grados).
  lon_2: Longitud de la segunda coordenada (en grados).
  orientacion_camara: Orientación de la cámara (en grados).

Returns:
  Angulo de rotación horizontal (en grados).
"""
def calcular_angulo_rotacion(lat_origen, lon_origen, lat_1, lon_1, lat_2, lon_2):
  # Convertir coordenadas a radianes
  lat_origen_rad = lat_origen * math.pi / 180
  lon_origen_rad = lon_origen * math.pi / 180
  lat_1_rad = lat_1 * math.pi / 180
  lon_1_rad = lon_1 * math.pi / 180
  lat_2_rad = lat_2 * math.pi / 180
  lon_2_rad = lon_2 * math.pi / 180

  # Calcular diferencias de longitud y latitud
  delta_lon = lon_2_rad - lon_1_rad
  delta_lat = lat_2_rad - lat_1_rad

  # Convertir diferencias a distancias en metros
  a = 6371000 * math.cos(lat_1_rad)
  b = 6371000

  distancia_x = delta_lon * a
  distancia_y = delta_lat * b

  # Calcular el ángulo de rotación (en radianes)
  angulo_rotacion_rad = math.atan2(distancia_y, distancia_x)

  # Convertir el ángulo a grados y ajustar la orientación
  angulo_rotacion_grados = angulo_rotacion_rad * 180 / math.pi

  # Calcular la orientación de la cámara (hacia la primera coordenada)
  orientacion_camara = math.atan2(lon_1_rad - lon_origen_rad, lat_1_rad - lat_origen_rad) * 180 / math.pi

  # Ajustar el rango del ángulo
  print(orientacion_camara)
  print(angulo_rotacion_grados)
  angulo_rotacion_ajustado = angulo_rotacion_grados - orientacion_camara
  if angulo_rotacion_ajustado < 0:
    angulo_rotacion_ajustado += 360
  elif angulo_rotacion_ajustado > 360:
    angulo_rotacion_ajustado -= 360

  return angulo_rotacion_ajustado




if __name__ == '__main__':
  # Ejemplo de uso
  lat_origen = 10.365080019445864  # Latitud del punto de origen
  lon_origen = -66.97754352980363  # Longitud del punto de origen
  lat_1 = 10.364582423561325  # Latitud de la primera coordenada
  lon_1 = -66.9775971650061  # Longitud de la primera coordenada
  lat_2 = 10.364741602457904  # Latitud de la segunda coordenada
  lon_2 =  -66.97789948094221  # Longitud de la segunda coordenada
  lat_derecha_3 = 10.365002407377682 
  lon_derecha_3 = -66.97747825401783
  lat_atras_4 = 10.365233330828088
  lon_atras_4 = -66.97767609475204
  coordenada_pan_1 = 0.565

  angulo_rotacion = calcular_angulo_rotacion(lat_origen, lon_origen, lat_1, lon_1, lat_2, lon_2)

  print("Angulo de rotación horizontal en sentido antihorario:", angulo_rotacion)

  pan_transformada = (360 - angulo_rotacion) / 360
  print("Pan de 0 fuera el punto inicial de la camara:", pan_transformada)

  pan_transformada = pan_transformada + coordenada_pan_1
  print("Pan de movimiento para la camara:", pan_transformada)
