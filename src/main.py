from robot.robot import Robot

def main():
    robot = Robot(start_position=(0, 0), max_velocity=1.0)

    robot.pick_up_cup()
    robot.move((1, 0), velocity=0.5)

    print("Position:", robot.position)
    print("Velocity:", robot.velocity)
    print("Has cup:", robot.has_cup)

if __name__ == "__main__":
    main()