from setuptools import setup

package_name = 'jetbot_delivery'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    py_modules=[],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Yoka',
    maintainer_email='you@example.com',
    description='Jetbot delivery mission nodes',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'delivery_node = jetbot_delivery.delivery_node:main',
            'buzzer_node = jetbot_delivery.buzzer_node:main',
            'arm_controller = jetbot_delivery.arm_controller:main',
        ],
    },
)
