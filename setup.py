from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mpra",
    version="0.2.1",
    description="A utility package with various file and directory management features.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Manoj Pennada",
    author_email="manojpennada@gmail.com",
    url="https://github.com/ManojPennada/mpra",
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

