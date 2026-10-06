import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

MIN_TEMP = 18.0
MAX_TEMP = 28.0

class TempMonitor(Node):
    def __init__(self):
        super().__init__('temp_monitor')
        self.subscription = self.create_subscription(
            Float32,
            'temperature',
            self.temperature_callback,
            10)
        self.subscription

    def temperature_callback(self, msg):
        temperature = msg.data
        if temperature < MIN_TEMP:
            self.get_logger().warn(f'Temperature too low: {temperature:.2f}°C')
        elif temperature > MAX_TEMP:
            self.get_logger().warn(f'Temperature too high: {temperature:.2f}°C')
        else:
            self.get_logger().info(f'Temperature is normal: {temperature:.2f}°C')

def main(args=None):
    rclpy.init(args=args)
    temp_monitor = TempMonitor()
    rclpy.spin(temp_monitor)
    temp_monitor.destroy_node()
    rclpy.shutdown()