from robot.robot import Robot
from control.controller import SafeMotionController


def main():
    robot = Robot(start_position=(0, 0), max_velocity=1.0)
    controller = SafeMotionController(
        max_velocity=1.0,
        max_acceleration=0.2
    )

    robot.pick_up_cup()

    desired_velocities = [0.0, 1.0, 1.0, 0.0]

    for v in desired_velocities:
        safe_v = controller.compute_velocity(v)
        robot.move(robot.position, safe_v)
        print(f"Safe velocity: {safe_v:.2f}")


if __name__ == "__main__":
    main()