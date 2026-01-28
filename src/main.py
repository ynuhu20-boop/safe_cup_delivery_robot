from robot.robot import Robot
from control.controller import SafeMotionController
from planning.planner import PointToPointPlanner


def main():
    # Initialize robot
    robot = Robot(start_position=(0.0, 0.0), max_velocity=1.0)

    # Initialize safe motion controller
    controller = SafeMotionController(
        max_velocity=1.0,
        max_acceleration=0.2
    )

    # Pick up the cup (start delivery)
    robot.pick_up_cup()

    # Define goal and planner
    goal = (2.0, 0.0)
    planner = PointToPointPlanner(goal=goal)

    print("Starting safe cup delivery...\n")

    # Simulation loop
    for step in range(30):
        direction, desired_velocity = planner.compute_direction_and_speed(
            robot.position
        )

        safe_velocity = controller.compute_velocity(desired_velocity)
        robot.move(direction, safe_velocity)

        print(
            f"Step {step:02d} | "
            f"Position: {robot.position} | "
            f"Velocity: {safe_velocity:.2f}"
        )

        # Stop if reached goal
        if safe_velocity == 0.0:
            print("\nGoal reached safely. Delivery complete.")
            break


if __name__ == "__main__":
    main()
