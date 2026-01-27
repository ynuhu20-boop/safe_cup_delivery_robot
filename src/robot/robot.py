class Robot:
    def __init__(self, start_position, max_velocity):
        self.position = start_position  # (x, y)
        self.velocity = 0.0
        self.max_velocity = max_velocity
        self.has_cup = False

    def pick_up_cup(self):
        self.has_cup = True

    def drop_cup(self):
        self.has_cup = False

    def move(self, new_position, velocity):
        if velocity > self.max_velocity:
            raise ValueError("Velocity exceeds safe limit")

        self.position = new_position
        self.velocity = velocity
