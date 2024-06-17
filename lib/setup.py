from setuptools import setup, find_packages

setup(
    name='restaurant-reservation',
    version='1.0.0',
    description='CLI application for a restaurant reservation system',
    author='Your Name',
    author_email='your_email@example.com',
    packages=find_packages(),
    install_requires=[
        'SQLAlchemy==1.4.37',
        'pytest==6.2.5',
    ],
    entry_points={
        'console_scripts': [
            'restaurant-reservation = restaurant_reservation.main:main',
        ],
    },
)
