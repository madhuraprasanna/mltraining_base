from setuptools import setup, find_packages

def read_requirements():
    """Read requirements from requirements.txt file"""
    with open('requirements.txt', 'r') as file:
        return [line.strip() for line in file if line.strip() and not line.startswith('#')]

setup(
    name="mltraining_wsp2",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=read_requirements(),
    python_requires='>=3.8',
    author="Your Name",
    description="ML Training Workspace for Churn Prediction",
    long_description="A machine learning project for customer churn prediction using DVC and MLflow",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)