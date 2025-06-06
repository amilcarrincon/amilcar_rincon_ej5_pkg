import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_srvs.srv import Empty

class ContadorPublisher(Node):
    def __init__(self):
        super().__init__('contador_publisher')
        self.declare_parameter('frecuencia', 5.0)
        self.declare_parameter('maximo', 100)

        self.frecuencia = self.get_parameter('frecuencia').value
        self.maximo = self.get_parameter('maximo').value
        self.contador = 0

        self.pub = self.create_publisher(Int32, 'contador', 10)
        self.timer = self.create_timer(1.0 / self.frecuencia, self.publicar)
        self.srv = self.create_service(Empty, 'resetear_contador', self.callback_reset)

    def publicar(self):
        if self.contador <= self.maximo:
            msg = Int32()
            msg.data = self.contador
            self.pub.publish(msg)
            self.get_logger().info(f'Contador: {self.contador}')
            self.contador += 1

    def callback_reset(self, request, response):
        self.get_logger().info('Contador reiniciado.')
        self.contador = 0
        return response

def main(args=None):
    rclpy.init(args=args)
    node = ContadorPublisher()
    rclpy.spin(node)
    rclpy.shutdown()
