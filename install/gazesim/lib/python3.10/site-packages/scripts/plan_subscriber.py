#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path

class PlanSubscriber(Node):
    def __init__(self):
        super().__init__('plan_subscriber')
        # Előfizetés a /plan topikra
        self.subscription = self.create_subscription(
            Path,
            '/plan',
            self.plan_callback,
            10
        )
        self.path_coords = []  # Az optimális útvonal koordinátái

    def plan_callback(self, msg):
        """ Callback függvény a /plan topikhoz """
        self.path_coords = [(pose.pose.position.x, pose.pose.position.y) for pose in msg.poses]
        self.get_logger().info(f'Received path with {len(self.path_coords)} points.')
        print(self.path_coords)  # Kiírás ellenőrzéshez

def main(args=None):
    rclpy.init(args=args)
    node = PlanSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
