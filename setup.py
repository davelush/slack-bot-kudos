try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name="SlackBotSandbox",
    version="0.0.1-snapshot",
    license='Apache License 2.0',
    packages=find_packages(),
    package_dir={'slack_bot': 'slack_bot', 'kudos': 'kudos'},
    long_description=open('README.md').read(),
    test_suite='tests',
    setup_requires=['pytest-runner'],
    install_requires=['PyYAML']
)