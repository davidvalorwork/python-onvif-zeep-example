import math
from geopy.distance import geodesic
from typing import Tuple

def calcular_angulo_rotacion(origen: Tuple[float, float], referencia: Tuple[float, float], emergencia: Tuple[float, float], ref_pan: float):
  a = geodesic(origen, referencia).meters
  b = geodesic(origen, emergencia).meters
  c = geodesic(referencia, emergencia).meters

  cosine_theorem = math.acos(((a * a) + (b * b) - (c*c)) / (2 * a * b))
  print(f"Distance a (origen to referencia): {a} meters, Coordinates: origen to referencia")
  print(f"Distance b (origen to emergencia): {b} meters, Coordinates: origen to emergencia")
  print(f"Distance c (referencia to emergencia): {c} meters, Coordinates: referencia to emergencia")
  print(f"Cosine theorem result: {cosine_theorem}")

  lat_diff_1, lon_diff_1 = origen[0] - referencia[0], origen[1] - referencia[1]
  lat_diff_2, lon_diff_2 = origen[0] - emergencia[0], origen[1] - emergencia[1]

  cross_product = (lat_diff_1 * lon_diff_2) - (lon_diff_1 * lat_diff_2)
  print(f"Cross product: {cross_product}")

  degrees = (cosine_theorem * 180) / math.pi
  print(f"Degrees: {degrees}")
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

  print("Resultado final: ", pan)
