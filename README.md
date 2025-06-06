# amilcar_rincon_ej5_pkg

Este paquete de ROS 2 contiene dos nodos en Python:

- `contador_node`: Publica un contador a una frecuencia configurable y tiene un servicio que permite reiniciar el contador.
- `monitor_node`: Se suscribe al contador y cuando detecta que ha alcanzado un valor específico (configurable), llama al servicio para reiniciar el contador.

## Estructura
amilcar_rincon_ej5_pkg/
├── amilcar_rincon_ej5_pkg/
│ ├── init.py
│ ├── contador_node.py
│ └── monitor_node.py
├── launch/
│ └── launch_ejercicio.py
├── package.xml
└── setup.py


## Dependencias

Este paquete depende de:

- `rclpy`
- `std_msgs`
- `std_srvs`

Instálalo dentro de tu workspace de ROS 2 (`~/ros2_ws`):

```bash
cd ~/ros2_ws
colcon build
source install/setup.bash

# Ejecución
Puedes lanzar ambos nodos con:

ros2 launch amilcar_rincon_ej5_pkg launch_ejercicio.py

