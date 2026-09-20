from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'temp_monitor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')), 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Szabo Mate',
    maintainer_email='mate.szabo1215@gmail.com',
    description='Simple ROS 2 package: simulated temperature generator and monitor',
    license='GNU General Public License v3.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'temp_generator = temp_monitor.temp_generator:main',
            'temp_monitor = temp_monitor.temp_monitor:main',
        ],
    },
)
