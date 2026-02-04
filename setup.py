# To install local package in my virtual environment I'd be using this setup.py file

from setuptools import setup, find_packages

setup(
    name="mcqgen",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "openRouter",
        "streamlit",
        "langchain",
        "pyPDF2",
        "python-dotenv",
    ],

)
