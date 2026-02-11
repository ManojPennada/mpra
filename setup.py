from setuptools import setup, find_packages

setup(
    name="mpra",
    version="0.2.0",
    description="A utility package with various file and directory management features.",
    author="Manoj Pennada",
    author_email="manojpennada@gmail.com",
    packages=find_packages(),
    install_requires=[],
    extras_require={
        'excel': ['openpyxl'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

