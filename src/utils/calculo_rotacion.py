import math
from geopy.distance import geodesic

def calcular_angulo_rotacion(origen, referencia, emergencia):

  # Formula de Haversine
  haversine_cateto_origen_referencia = geodesic(origen, referencia).meters
  print("haversine_cateto_origen_referencia:",haversine_cateto_origen_referencia)
  a = haversine_cateto_origen_referencia

  haversine_cateto_origen_emergencia = geodesic(origen, emergencia).meters
  print("haversine_cateto_origen_emergencia3:",haversine_cateto_origen_emergencia)
  b = haversine_cateto_origen_emergencia

  haversine_cateto_referencia_emergencia = geodesic(referencia, emergencia).meters
  print("haversine_cateto_referencia_emergencia2:",haversine_cateto_referencia_emergencia)
  c = haversine_cateto_referencia_emergencia

  # angulo_rotacion_rad = math.atan2(delta_lon, delta_lat)
  teorema_del_coseno = ((a * a) + (b * b) - (c*c))/(2 * a * b)
  teorema_del_coseno = math.acos(teorema_del_coseno)
  print("TEOREMA COSENO", teorema_del_coseno)

  lat_org_1 = origen[0] - referencia[0]
  lon_org_1 = origen[1] - referencia[1]

  lat_org_2 = origen[0] - emergencia[0]
  lon_org_2 = origen[1] - emergencia[1]
  
  producto_cruz= (lat_org_1 * lon_org_2) - (lon_org_1 * lat_org_2)
  print("SI POSITIVO HORARIO SI NEGATIVO ANTIHORARIO",producto_cruz)

  # Convertir el ángulo a grados
  angulo_rotacion_grados_teorema_coseno = (teorema_del_coseno * 180) / math.pi

  print("angulo_rotacion_grados_teorema_coseno:",angulo_rotacion_grados_teorema_coseno)
  return angulo_rotacion_grados_teorema_coseno




if __name__ == '__main__':
  # Ejemplo de uso
  origen = (10.365072129702737, -66.9775462486802)
  referencia = (10.364764751417162, -66.97756636524517)
  bocono = (10.36500155145449, -66.97778161250672)
  meta = (10.365006828332977, -66.97706278051929)
  berta = (10.365654678419954, -66.97793301987491)
  simoncito = (10.366454368101305, -66.97769878433466)
  pao = (10.366164343123057, -66.97679802169682)
  coordenada_pan_1 = 0.565

  # angulo_rotacion = calcular_angulo_rotacion(origen, referencia, bocono)
  # angulo_rotacion = calcular_angulo_rotacion(origen, referencia, meta)
  # angulo_rotacion = calcular_angulo_rotacion(origen, referencia, simoncito)
  angulo_rotacion = calcular_angulo_rotacion(origen, referencia, berta)
  # angulo_rotacion = calcular_angulo_rotacion(origen, referencia, pao)

  print("Angulo de rotación horizontal en sentido antihorario:", angulo_rotacion)

  pan_transformada = (360 - angulo_rotacion) / 360
  print("Pan de 0 fuera el punto inicial de la camara:", pan_transformada)

  pan_transformada = pan_transformada + coordenada_pan_1
  print("Pan de movimiento para la camara:", pan_transformada)
