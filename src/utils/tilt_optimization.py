from geopy.distance import geodesic

def tilt_optimization_function(min, tilt_optimization, altura, camera, emergencia):
  distance = geodesic(camera, emergencia).meters
  if distance < min:
    return altura
  else:
    return altura * tilt_optimization
  