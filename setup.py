from setuptools import setup
from masonite.info import VERSION

setup(
    name='masonite',
    packages=[
        'masonite',
        'masonite.auth',
        'masonite.facades',
        'masonite.providers',
        'masonite.commands',
        'masonite.drivers',
        'masonite.managers',
        'masonite.testsuite',
        'masonite.queues',
        'masonite.contracts',
        'masonite.contracts.managers',
        'masonite.helpers',
    ],
    version=VERSION,
    install_requires=[
        'validator.py>=1.2,<1.3',
        'cryptography>=2.3,<2.4',
        'bcrypt>=3.1,<3.2',
        'requests>=2.0,<2.99',
        'tldextract>=2.2,<2.3',
        'Jinja2>=2,<3',
        'python-dotenv>=0.8,<0.9',
        'passlib>=1.7,<1.8',
        'whitenoise>=3.3,<3.4',
        'pytest>=3,<4',
        'masonite-entry>=0.0.0,<=0.9.99',
        'masonite-scheduler>=1.0.0,<=1.0.99',
        'pendulum>=1.5,<1.6',
        'cleo>=0.6,<0.7',
        'tabulate>=0.8,<0.9',
        'watchdog>=0.8,<0.9',
        'waitress>=1.1,<1.2',
        'psutil>=5.4,<5.5',
    ],
    extra_requires={
        ':python_version == "3.4"': [
            'orator==0.9.7',
        ],
        ':python_version >= "3.5"': [
            'orator>=0.9,<0.99',
        ]
    },
    description='The core for the Masonite framework',
    author='Joseph Mancuso',
    author_email='idmann509@gmail.com',
    url='https://github.com/MasoniteFramework/masonite',
    keywords=['python web framework', 'python3', 'masonite'],
    classifiers=[],
    include_package_data=True,
)
