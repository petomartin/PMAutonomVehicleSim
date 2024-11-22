import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from pynput import keyboard

class KeyboardController(Node):
    def __init__(self):
        super().__init__('keyboard_controller')
        self.publisher = self.create_publisher(Twist, '/car_lexus/cmd_vel', 10)
        self.velocity_msg = Twist()
        self.listener = keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_release)
        self.listener.start()

    def on_key_press(self, key):
        try:
            if key.char == 'w':  # Előre
                self.velocity_msg.linear.x = 1.0
            elif key.char == 's':  # Hátra
                self.velocity_msg.linear.x = -1.0
            elif key.char == 'a':  # Balra
                self.velocity_msg.angular.z = 1.0
            elif key.char == 'd':  # Jobbra
                self.velocity_msg.angular.z = -1.0
        except AttributeError:
            pass  # Ha nem karaktert nyomtak meg, akkor nem csinálunk semmit
        self.publisher.publish(self.velocity_msg)

    def on_key_release(self, key):
        try:
            if key.char in ['w', 's']:
                self.velocity_msg.linear.x = 0.0
            elif key.char in ['a', 'd']:
                self.velocity_msg.angular.z = 0.0
        except AttributeError:
            pass  # Ha nem karaktert nyomtak meg, akkor nem csinálunk semmit
        self.publisher.publish(self.velocity_msg)

def main(args=None):
    rclpy.init(args=args)
    controller = KeyboardController()
    rclpy.spin(controller)
    controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
