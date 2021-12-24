from setuptools import find_packages, setup

setup(
    name="recipe_reduce",
    version="0.0.1",
    author="Qibin Chen",
    author_email="qibinc@andrew.cmu.edu",
    license="MIT",
    python_requires=">=3.8",
    packages=find_packages(exclude=[]),
    install_requires=[
        "black>=21.10b0",
        "isort>=5.8.0",
        "pre-commit>=2.15.0",
        "pytest>=6.2.4",
        "tabulate>=0.8.9",
    ],
)
