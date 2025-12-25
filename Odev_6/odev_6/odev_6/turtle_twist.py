import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleTwist(Node):
    def __init__(self):
        super().__init__('turtle_twist_node')
        
        #1.Parametre Tanımlama
        #linear_speed ve angular_speed parametrelerini default değerleriyle tanımlıyoruz
        self.declare_parameter('linear_speed', 1.5)
        self.declare_parameter('angular_speed', 1.0)
        
        # /turtle1/cmd_vel topicine Twist tipi mesaj göndermek için publisher oluştur
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
        #timer ile periyodik görev / saniye cinsinden 
        timer_period = 0.5 
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        self.get_logger().info('Turtle Twist Düğümü Başlatıldı')

    def timer_callback(self):
        #çalışma anında parametreleri oku(bunlar terminalden değiştirilebilir)
        v = self.get_parameter('linear_speed').get_parameter_value().double_value
        
        w = self.get_parameter('angular_speed').get_parameter_value().double_value
        
        #Twist mesajı oluşturma ve değerleri atama
        msg = Twist()
        msg.linear.x = v 
        msg.angular.z = w
        
        #mesajı yayınlama
        self.publisher_.publish(msg)
        self.get_logger().info(f'Hız: v={v}, w={w}')

    def stop_turtle(self):
        stop_msg = Twist()
        self.publisher_.publish(stop_msg)
        self.get_logger().warn('Turtle durduruluyor...')

def main(args=None):
    rclpy.init(args=args) #ROS2 başlat
    node = TurtleTwist() #node oluşturma
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
    	#ctrl+c ile 
        node.stop_turtle()
    finally:
        node.destroy_node()
        rclpy.shutdown()
