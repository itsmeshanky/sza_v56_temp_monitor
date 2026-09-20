import random

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class TemperatureGenerator(Node):
    def __init__(self):
        super().__init__('temperature_generator')
        self.publisher_ = self.create_publisher(Float32, 'temperature', 10)
        self.timer = self.create_timer(1.0, self.publish_temperature)

    def publish_temperature(self):
        temperature = random.uniform(20.0, 30.0)  # Simulate temperature between 20 and 30 degrees Celsius
        msg = Float32()
        msg.data = temperature
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {temperature:.2f} °C')

def main(args=None):
    rclpy.init(args=args)
    temperature_generator = TemperatureGenerator()
    rclpy.spin(temperature_generator)
    temperature_generator.destroy_node()
    rclpy.shutdown()