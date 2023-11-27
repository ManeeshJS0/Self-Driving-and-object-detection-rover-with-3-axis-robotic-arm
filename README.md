Autonomous Rover with Robotic Arm
Overview
This project is an autonomous rover equipped with a robotic arm capable of object detection and manipulation. The rover is designed to navigate its environment, detect objects using a pre-trained model, and perform tasks with its robotic arm. The code is written in Python and utilizes Raspberry Pi GPIO for hardware control.

Features
Motor Control: Control the movement of the rover using PWM-controlled motors.
Robotic Arm: Manipulate objects with a 3-axis robotic arm featuring servo motors and a gripper.
Object Detection: Utilize a pre-trained Faster R-CNN model for real-time object detection.
Self-Driving Logic: Implement self-driving capabilities based on joystick input and pixel summation for path detection.
Hardware Requirements
Raspberry Pi 4B
DC Motors (4)
Motor Controller (L298M)
Servo Motors (5)
Gripper
12V Battery
Software Requirements
Python
Pygame
OpenCV
TensorFlow or PyTorch (for object detection)

Setup and Usage
Clone this repository to your Raspberry Pi:


1. pip install -r requirements.txt
Connect the hardware components following the provided pin configurations.

2. python main.py
The rover will start its autonomous navigation and object manipulation.

Customization
Feel free to customize the code to fit your specific rover configuration or add new features. Refer to the code comments and module descriptions for guidance.

Contributing
If you have improvements or additional features to suggest, feel free to open an issue or submit a pull request.

