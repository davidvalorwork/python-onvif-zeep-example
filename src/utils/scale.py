def scale_angle_0to1(angle: float, ref_pan: float, cross: float) -> float:
    print(f"Original angle: {angle}")
    pan = angle / 360
    print(f"Scaled angle (0 to 1): {pan}")
    pan = ref_pan + pan if cross > 0 else ref_pan - pan
    print(f"Adjusted pan with ref_pan and cross: {pan}")
    return pan

def scale_angle_less1to1(angle: float, ref_pan: float, cross: float) -> float:
    print(f"Original angle: {angle}")
    pan_angle = (angle * 2 / 360)
    print(f"Initial pan_angle (less 1 to 1): {pan_angle}")
    pan = ref_pan + pan_angle if cross > 0 else ref_pan - pan_angle
    print(f"Before adjustment: pan = {pan}")
    if(pan > 1): 
        print("Pan exceeded 1, adjusting...")
        pan = pan - 2
        print(f"After adjustment: pan = {pan}")
    print(f"Adjusted pan with ref_pan, cross, and correction: {pan}")
    return pan

def scale_angle_less1to1_90degresstilt(angle: float) -> float:
    scaled_angle = (angle * 2 / 90) -1
    print(f"Scaled angle for less1to1 90 degrees tilt: {scaled_angle}")
    return scaled_angle

def scale_angle_90degresstilt(angle: float) -> float:
    scaled_angle = angle / 90
    print(f"Scaled angle for 90 degrees tilt: {scaled_angle}")
    return scaled_angle