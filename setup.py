from setuptools import find_packages, setup

package_name = 'amilcar_rincon_ej5_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/launch_ejercicio.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='amilcar.rincon.charris@gmail.com',
    description='Paquete ROS 2 con contador y monitor que reinicia por servicio',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'contador_node = amilcar_rincon_ej5_pkg.contador_node:main',
            'monitor_node = amilcar_rincon_ej5_pkg.monitor_node:main',
        ],
    },
)
