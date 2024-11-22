import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile
import sys
import tty
import termios

class TeleopNode(Node):
    def __init__(self):
        super().__init__('teleop_node')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', QoSProfile(depth=10))
        self.timer = self.create_timer(0.1, self.timer_callback)

        # Készítsd elő a Twist üzenetet
        self.cmd = Twist()

    def timer_callback(self):
        self.publisher_.publish(self.cmd)
        self.get_logger().info(f'Publishing: Linear: {self.cmd.linear.x}, Angular: {self.cmd.angular.z}')

    def get_key(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        tty.setraw(sys.stdin.fileno())
        try:
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def run(self):
        self.get_logger().info("Use 'w' to move forward, 's' to move backward, 'a' to turn left, 'd' to turn right, 'x' to stop.")
        while rclpy.ok():
            key = self.get_key()
            if key == 'w':
                self.cmd.linear.x = 0.5
                self.cmd.angular.z = 0.0
            elif key == 's':
                self.cmd.linear.x = -0.5
                self.cmd.angular.z = 0.0
            elif key == 'a':
                self.cmd.linear.x = 0.0
                self.cmd.angular.z = 1.0
            elif key == 'd':
                self.cmd.linear.x = 0.0
                self.cmd.angular.z = -1.0
            elif key == 'x':
                self.cmd.linear.x = 0.0
                self.cmd.angular.z = 0.0
            else:
                continue  # Ha más gombot nyomsz, folytasd

            self.timer_callback()  # Publikáld a frissített üzenetet

def main(args=None):
    rclpy.init(args=args)
    teleop_node = TeleopNode()
    try:
        teleop_node.run()
    except KeyboardInterrupt:
        pass
    finally:
        teleop_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
