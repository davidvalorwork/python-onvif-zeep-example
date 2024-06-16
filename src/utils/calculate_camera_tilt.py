import math
from geopy.distance import geodesic

def calculate_camera_tilt(coord1: tuple, coord2: tuple, altura: float) -> float:
  # Calculate the distance using geodesic
  distance = geodesic(coord1, coord2).meters

  # Cosine theorem to calculate the angle
  third_side = math.sqrt(distance**2 + altura**2)

  cos_angle = (altura**2 + third_side**2 - distance**2) / (2 * altura * third_side)
  angulo = math.degrees(math.acos(cos_angle))

  return angulo

if __name__ == '__main__':
    coord1 = (40.7128, -74.0060)  # Original location
    coord2 = (40.7128, -74.0059)  # Approximately 10 meters east of the original location
    altura = 1  # 100 meters

    expected_angle = 0.07957747154594767  # This is the expected result. You might need to adjust this based on your calculations.
    actual_angle = calculate_camera_tilt(coord1, coord2, altura)

    print(f'Expected {expected_angle}, but got {actual_angle}')