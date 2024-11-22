import rclpy
from rclpy.node import Node

class StatusLoggerNode(Node):
    def __init__(self):
        super().__init__('status_logger_node')
        self.get_logger().info("Szimuláció elindult és minden rendben van.")

def main(args=None):
    rclpy.init(args=args)
    node = StatusLoggerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
