import math
from geopy.distance import geodesic

def calculate_camera_tilt(coord1: tuple, coord2: tuple, altura: float) -> float:
  print("Calculating camera tilt...")

  # Calculate the distance using geodesic
  b = geodesic(coord1, coord2).meters
  print(f"Distance between coordinates tilt: {b}")
  
  # Cosine theorem to calculate the angle
  a = altura
  c = math.sqrt(a**2 + b**2)
  
  cos_angle = (a**2 + c**2 - b**2) / (2 * a * c)
  angulo = math.degrees(math.acos(cos_angle))

  print(f"Calculated camera tilt: {angulo}")

  return angulo

if __name__ == '__main__':
    coord1 = (40.7128, -74.0060)  # Original location
    coord2 = (40.7128, -74.0059)  # Approximately 10 meters east of the original location
    altura = 1  # 100 meters

    expected_angle = 0.07957747154594767  # This is the expected result. You might need to adjust this based on your calculations.
    actual_angle = calculate_camera_tilt(coord1, coord2, altura)

    print(f'Expected {expected_angle}, but got {actual_angle}')