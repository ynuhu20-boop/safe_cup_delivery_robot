class SafeMotionController:
    def __init__(self, max_velocity, max_acceleration):
        self.max_velocity = max_velocity
        self.max_acceleration = max_acceleration
        self.previous_velocity = 0.0

    def compute_velocity(self, desired_velocity):
        # Clamp velocity
        desired_velocity = min(desired_velocity, self.max_velocity)

        # Compute acceleration
        acceleration = desired_velocity - self.previous_velocity

        if abs(acceleration) > self.max_acceleration:
            # Limit acceleration
            acceleration = (
                self.max_acceleration
                if acceleration > 0
                else -self.max_acceleration
            )

        safe_velocity = self.previous_velocity + acceleration
        self.previous_velocity = safe_velocity

        return safe_velocity
