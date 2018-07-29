try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='RethinkPool',
    version='0.4.2',
    packages=['rethinkpool'],
    url='https://github.com/momothereal/RethinkPool',
    license='Apache License v2',
    author='Shiqiao Du',
    author_email='lucidfrontier.45@gmail.com',
    description='RethinkDB Connection Pool for Python',
    install_requires=["future", "rethinkdb"]
)
