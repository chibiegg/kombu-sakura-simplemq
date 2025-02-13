from setuptools import setup, find_packages

setup(
    name="kombu-sakura-simplemq",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["kombu", "requests"],
)
