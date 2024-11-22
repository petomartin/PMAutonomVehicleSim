import rclpy
from rclpy.node import Node

class SensorHandlerNode(Node):
    def __init__(self):
        super().__init__('sensor_handler')
        self.get_logger().info('Szenzorok figyelése elindult!')
        # Itt beállíthatod a szenzorok előfizetését
        # pl. self.create_subscription(...)

def main(args=None):
    rclpy.init(args=args)
    node = SensorHandlerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
