import math
from geopy.distance import geodesic
from typing import Tuple

def calcular_angulo_rotacion(origen: Tuple[float, float], referencia: Tuple[float, float], emergencia: Tuple[float, float], ref_pan: float):
  # Calculate distances using Haversine formula
  a = geodesic(origen, referencia).meters  # Distance between origin and reference
  b = geodesic(origen, emergencia).meters  # Distance between origin and emergency
  c = geodesic(referencia, emergencia).meters  # Distance between reference and emergency

  # Calculate cosine theorem
  cosine_theorem = math.acos(((a * a) + (b * b) - (c*c)) / (2 * a * b))
  print(f"Cosine theorem result: {cosine_theorem}")

  # Calculate differences in latitude and longitude for origin-reference and origin-emergency
  lat_diff_1, lon_diff_1 = origen[0] - referencia[0], origen[1] - referencia[1]
  lat_diff_2, lon_diff_2 = origen[0] - emergencia[0], origen[1] - emergencia[1]

  # Calculate cross product to determine rotation direction
  cross_product = (lat_diff_1 * lon_diff_2) - (lon_diff_1 * lat_diff_2)
  print(f"Rotation direction (positive for clockwise, negative for counterclockwise): {cross_product}")
  
  # Convert angle to degrees and calculate transformed pan
  degrees = (cosine_theorem * 180) / math.pi
  return [degrees, cross_product]




if __name__ == '__main__':
  # Ejemplo de uso
  origen = (10.365072129702737, -66.9775462486802)
  referencia = (10.364764751417162, -66.97756636524517)
  bocono = (10.36500155145449, -66.97778161250672)
  meta = (10.365006828332977, -66.97706278051929)
  berta = (10.365654678419954, -66.97793301987491)
  simoncito = (10.366454368101305, -66.97769878433466)
  pao = (10.366164343123057, -66.97679802169682)
  coordenada_pan_referencia = 0.565

  pan = calcular_angulo_rotacion(origen, referencia, bocono, coordenada_pan_referencia)
  # pan = calcular_angulo_rotacion(origen, referencia, meta, coordenada_pan_referencia)
  # pan = calcular_angulo_rotacion(origen, referencia, simoncito, coordenada_pan_referencia)
  # pan = calcular_angulo_rotacion(origen, referencia, berta, coordenada_pan_referencia)
  # pan = calcular_angulo_rotacion(origen, referencia, pao, coordenada_pan_referencia)

  print("Resultado final: ", pan)
