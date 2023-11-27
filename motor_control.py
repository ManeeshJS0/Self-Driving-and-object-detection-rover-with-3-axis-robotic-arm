import RPi.GPIO as GPIO
import pygame

class MotorControl:
    def __init__(self, left_pins, right_pins):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(left_pins + right_pins, GPIO.OUT)
        self.left_motor = GPIO.PWM(left_pins[0], 1000)
        self.right_motor = GPIO.PWM(right_pins[0], 1000)
        self.left_motor.start(0)
        self.right_motor.start(0)

    def set_speed(self, left_speed, right_speed):
        self.left_motor.ChangeDutyCycle(left_speed)
        self.right_motor.ChangeDutyCycle(right_speed)

    def stop_motors(self):
        self.set_speed(0, 0)

    def cleanup(self):
        GPIO.cleanup()


class JoystickControl:
    def __init__(self, joystick):
        self.joystick = joystick

    def get_axes(self):
        pygame.event.pump()
        left_right = self.joystick.get_axis(0)
        front_back = self.joystick.get_axis(1)
        return left_right, front_back
