try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

non_test_packages = [p for p in find_packages() if p.split('.')[-1] != 'tests']
requirements = []

setup(
    name="slack-bot-kudos",
    version="0.1",
    license='Apache License 2.0',
    packages=non_test_packages,
    long_description=open('README.md').read(),
    test_suite='tests',
    setup_requires=['pytest-runner'],
    install_requires=requirements
)