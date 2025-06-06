import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_srvs.srv import Empty

class MonitorSubscriber(Node):
    def __init__(self):
        super().__init__('monitor_subscriber')
        self.declare_parameter('valor_reinicio', 50)
        self.valor_reinicio = self.get_parameter('valor_reinicio').value

        self.cli = self.create_client(Empty, 'resetear_contador')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando servicio resetear_contador...')

        self.req = Empty.Request()
        self.sub = self.create_subscription(Int32, 'contador', self.callback, 10)

    def callback(self, msg):
        self.get_logger().info(f'Recibido: {msg.data}')
        if msg.data >= self.valor_reinicio:
            self.get_logger().info('Solicitando reinicio...')
            self.cli.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)
    node = MonitorSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()
