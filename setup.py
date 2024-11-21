from setuptools import setup, find_packages

setup(
    name="hornet_lang",
    version="0.1.0",
    packages=find_packages(),
    scripts=['bin/hornet'],
    install_requires=[],
    author="Your Name",
    description="A bee-themed programming language",
    python_requires=">=3.6",
)