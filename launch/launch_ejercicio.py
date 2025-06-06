from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('frecuencia', default_value='5.0'),
        DeclareLaunchArgument('valor_reinicio', default_value='50'),
        DeclareLaunchArgument('maximo', default_value='100'),

        Node(
            package='amilcar_rincon_ej5_pkg',
            executable='contador_node',
            name='nodo_contador',
            parameters=[{
                'frecuencia': LaunchConfiguration('frecuencia'),
                'maximo': LaunchConfiguration('maximo')
            }]
        ),

        Node(
            package='amilcar_rincon_ej5_pkg',
            executable='monitor_node',
            name='nodo_monitor',
            parameters=[{
                'valor_reinicio': LaunchConfiguration('valor_reinicio')
            }]
        ),
    ])
