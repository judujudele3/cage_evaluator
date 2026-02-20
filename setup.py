from setuptools import setup

package_name = 'cage_evaluator'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Cage Team',
    maintainer_email='todo@todo.com',
    description='Evaluation node for robotic arm performance in OptiTrack cage environment',
    license='MIT',
    entry_points={
        'console_scripts': [
        ],
    },
)