***Autonomous Rover with Robotic Arm***__


**Overview**
This project is an autonomous rover equipped with a robotic arm capable of object detection and manipulation. The rover is designed to navigate its environment, detect objects using a pre-trained model, and perform tasks with its robotic arm. The code is written in Python and utilizes Raspberry Pi GPIO for hardware control.

**Features**
1. Motor Control: Control the movement of the rover using PWM-controlled motors.
2. Robotic Arm: Manipulate objects with a 3-axis robotic arm featuring servo motors and a gripper.
3. Object Detection: Utilize a pre-trained Faster R-CNN model for real-time object detection.
4. Self-Driving Logic: Implement self-driving capabilities based on joystick input and pixel summation for path detection.

**Hardware Requirements**
1.Raspberry Pi 4B
2. DC Motors (4)
3. Motor Controller (L298M)
4. Servo Motors (5)
5. Gripper
6. 12V Battery
7. Software Requirements
8. Python
9. Pygame
10.OpenCV
11. TensorFlow or PyTorch (for object detection)

**Setup and Usage**
Clone this repository to your Raspberry Pi:

1. pip install -r requirements.txt
Connect the hardware components following the provided pin configurations.

2. python main.py
The rover will start its autonomous navigation and object manipulation.

**Customization**
Feel free to customize the code to fit your specific rover configuration or add new features. Refer to the code comments and module descriptions for guidance.

**Contributing**
If you have improvements or additional features to suggest, feel free to open an issue or submit a pull request.

