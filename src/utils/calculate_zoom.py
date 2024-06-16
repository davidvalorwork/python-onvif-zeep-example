from geopy.distance import geodesic

def calculate_zoom(coord1: tuple, coord2: tuple) -> float:
  # Calculate the distance between the two coordinates in meters
  distance = geodesic(coord1, coord2).meters

  # Define the zoom scale limits
  min_distance, max_distance = 30, 300

  # Calculate the zoom level
  if distance <= min_distance:
    zoom = 0
  elif distance >= max_distance:
    zoom = 1
  else:
    zoom = (distance - min_distance) / (max_distance - min_distance)

  return zoom