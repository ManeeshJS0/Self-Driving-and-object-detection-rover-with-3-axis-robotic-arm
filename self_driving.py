class SelfDrivingLogic:
    def __init__(self, speed=5, sensor_range=10):
        # Initialize any parameters or settings for self-driving
        self.speed = speed
        self.sensor_range = sensor_range

    def calculate_direction(self, joystick_input, sensor_reading):
        # Implement the self-driving logic and return the direction
        # For demonstration purposes, we'll use a basic logic based on joystick input and sensor readings

        left_right, front_back = joystick_input

        # Adjust these thresholds based on your joystick input range
        left_threshold = -0.5
        right_threshold = 0.5

        # If an obstacle is detected by the sensor, stop and avoid it
        if sensor_reading < self.sensor_range:
            return "stop"

        # Otherwise, use joystick input to determine direction
        if left_right < left_threshold:
            return "left"
        elif left_right > right_threshold:
            return "right"
        else:
            return "forward"

# Example usage
self_driving_logic = SelfDrivingLogic(speed=8, sensor_range=15)
joystick_input = (0.2, 0.0)  # Example joystick input, you can replace this with your actual input
sensor_reading = 12  # Example sensor reading, you can replace this with your actual sensor data
direction = self_driving_logic.calculate_direction(joystick_input, sensor_reading)

print(f"The calculated direction is: {direction}")
print(f"Current speed: {self_driving_logic.speed}")
print(f"Sensor range: {self_driving_logic.sensor_range}")
