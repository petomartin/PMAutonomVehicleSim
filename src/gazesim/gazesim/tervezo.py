#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
import matplotlib.pyplot as plt


class PlanSubscriber(Node):
    def __init__(self):
        super().__init__('plan_subscriber')
        # Előfizetés a /plan topikra (optimális út)
        self.plan_subscription = self.create_subscription(
            Path,
            '/plan',
            self.plan_callback,
            10
        )
        # Előfizetés a /current_pose topikra (aktuális pozíció)
        self.pose_subscription = self.create_subscription(
            PoseStamped,
            '/amcl_pose',
            self.pose_callback,
            10
        )

        self.path_coords = []  # Az optimális útvonal koordinátái
        self.current_position = None  # Az autó aktuális helyzete

        # Matplotlib inicializálása
        plt.ion()
        self.fig, self.ax = plt.subplots()
        self.line_path, = self.ax.plot([], [], color='blue', label='Optimális útvonal')
        self.point_car, = self.ax.plot([], [], 'go', label='Autó pozíció', markersize=10)
        self.ax.legend()
        self.ax.grid(True)
        self.ax.set_title('Optimális út és autó pozíció')
        self.ax.set_xlabel('X koordináták')
        self.ax.set_ylabel('Y koordináták')

    def plan_callback(self, msg):
        """Callback függvény az optimális útvonal frissítésére"""
        self.path_coords = [(pose.pose.position.x, pose.pose.position.y) for pose in msg.poses]
        self.get_logger().info(f'Received path with {len(self.path_coords)} points.')
        self.update_plot()

    def pose_callback(self, msg):
        """Callback függvény az aktuális pozíció frissítésére"""
        self.current_position = (msg.pose.position.x, msg.pose.position.y)
        self.get_logger().info(f'Received current position: {self.current_position}.')
        self.update_plot()

    def update_plot(self):
        """Az ábra frissítése"""
        self.ax.cla()
        if self.path_coords:
            x_coords, y_coords = zip(*self.path_coords)
            self.ax.plot(x_coords, y_coords, color='blue', label='Optimális útvonal')
        if self.current_position:
            self.ax.scatter(
                self.current_position[0],
                self.current_position[1],
                color='green',
                label='Autó pozíció',
                s=100
            )
        self.ax.legend()
        self.ax.grid(True)
        self.ax.set_title('Optimális út és autó pozíció')
        self.ax.set_xlabel('X koordináták')
        self.ax.set_ylabel('Y koordináták')
        plt.pause(0.1)


def main(args=None):
    rclpy.init(args=args)
    node = PlanSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
        plt.ioff()
        plt.show()


if __name__ == '__main__':
    main()
