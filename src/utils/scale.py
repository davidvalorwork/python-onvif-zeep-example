def scale_angle_0to1(angle: float) -> float:
  return angle / 360

def scale_angle_less1to1(angle: float) -> float:
    return (angle / 180) -1 

def scale_angle_90degresstilt(angle: float) -> float:
    return angle / 90