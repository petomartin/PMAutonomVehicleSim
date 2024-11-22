import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan  # Válaszd ki a megfelelő szenzor típusokat
from geometry_msgs.msg import Twist  # A robot mozgását irányító üzenet

class PathPlanningNode(Node):
    def __init__(self):
        super().__init__('path_planning_node')
        
        # Iratkozz fel a szenzor adatokra
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',  # Itt add meg a megfelelő topik nevét
            self.listener_callback,
            10)
        
        # Publish egy Twist üzenet a robot irányításához
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)

    def listener_callback(self, msg):
        # Itt dolgozd fel a szenzor adatokat
        self.get_logger().info('Received sensor data')
        
        # Példa: egyszerű akadályelkerülő logika
        twist = Twist()
        if msg.ranges[0] < 1.0:  # Ha a középső szenzor túl közel van
            twist.angular.z = 1.0  # Fordulj el
        else:
            twist.linear.x = 0.5  # Haladj előre
        
        self.publisher.publish(twist)
        self.get_logger().info('Publishing movement command')

def main(args=None):
    rclpy.init(args=args)
    node = PathPlanningNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
