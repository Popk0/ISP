from setuptools import setup

setup(
    name='ser',
    version='1.0',
    description='l2',
    packages=['serializers'],
    author='Popk0',
    author_email='ilyamatveev12902@gmail.com',
    entry_points={
        'console_scripts': [
            'run = ser.main:main'
        ]
    }
)
