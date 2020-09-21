from setuptools import setup

setup(
    name = 'Downtime',
    version = '0.0.1',
    author = 'Rowan Reeve',
    description = 'Reminds you to take periodic breaks',
    license = 'BSD',
    install_requires = [
        'PySDL2',
        'dependency-injector'
    ]
)