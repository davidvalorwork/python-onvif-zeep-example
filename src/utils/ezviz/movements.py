def move_coordinates(camera, x, y):
    print("Moving to " + str(x) + ' ' + str(y))
    camera.move_coordinates(x,y)
    # multiple_movements(camera, 'up', 5, 10)
    # multiple_movements(camera, 'down', 1, int(10-(y*10)))

def multiple_movements(camera, direction, step, number):
    for x in range(number):
        camera.move(direction,step)