# amilcar_rincon_ej5_pkg

Este paquete de ROS 2 contiene dos nodos en Python:

- `contador_node`: Publica un contador a una frecuencia configurable y tiene un servicio que permite reiniciar el contador.
- `monitor_node`: Se suscribe al contador y cuando detecta que ha alcanzado un valor específico (configurable), llama al servicio para reiniciar el contador.

## 📦 Estructura

