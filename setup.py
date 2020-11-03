from setuptools import setup

setup(
    name='workout-gen',
    version='1.0.0',
    description='Generates some workout for the day',
    author='Djane Mabelin',
    author_email='thedjaney@gmail.com',
    install_requires=[],
    packages=['workout'],
    scripts=['generate-workout'],
    python_requires='>=3'
)