from setuptools import find_packages, setup

package_name = 'tf_broadcaster'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yufan',
    maintainer_email='yufan.fong@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'broadcaster = tf_broadcaster.broadcaster:main',
            'listener = tf_broadcaster.listener:main',
        ],
    },
)
