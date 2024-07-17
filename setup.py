from setuptools import setup, find_packages

setup(
    name="purifytext",
    version="0.1.0",
    author="Aman Kumar Jha",
    author_email="vats.amankumarjha2002@gmail.com",
    description="A package for cleaning and preprocessing text data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "beautifulsoup4",
        "nltk",
        "contractions",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
