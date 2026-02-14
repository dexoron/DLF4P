from setuptools import find_packages, setup
from dlf4p.config import VERSION


def readme():
    with open("README.md", "r", encoding="utf-8") as readme_file:
        return readme_file.read()


setup(
    name="dlf4p",
    version=VERSION,
    author="Dexoron",
    author_email="main@dexoron.su",
    description="Dexoron Logging Framework for Python",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://gitlab.com/dexoron/dlf4p",
    packages=find_packages(),
    install_requires=[],
    extras_require={
        "dev": ["pytest", "ruff"],
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: 3.15",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="logging logger dlf dexoron",
    project_urls={
        "Homepage": "https://dexoron.su",
        "Repository": "https://gitlab.com/dexoron/dlf4p",
    },
    python_requires=">=3.8",
)
