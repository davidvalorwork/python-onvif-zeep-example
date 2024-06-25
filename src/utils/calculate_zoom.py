from geopy.distance import geodesic

def calculate_zoom(coord1: tuple, coord2: tuple, min_distance: float, max_distance: float) -> float:
  # Calculate the distance between the two coordinates in meters
  distance = geodesic(coord1, coord2).meters

  # Calculate the zoom level
  if distance <= min_distance:
    zoom = 0
  elif distance >= max_distance:
    zoom = 1
  else:
    zoom = (distance - min_distance) / (max_distance - min_distance)

  return zoom