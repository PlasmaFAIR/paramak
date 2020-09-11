import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="paramak",
    version="0.0.13",
    author="Jonathan Shimwell",
    author_email="jonathan.shimwell@ukaea.uk",
    description="Create 3D fusion reactor CAD models based on input parameters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ukaea/paramak",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    tests_require=[
        "pytest-cov",
        "pytest-runner",
    ],
    install_requires=[
        "pytest-cov",
        "plotly",
        "scipy",
        "sympy",
        "numpy",
        "tqdm",
        "matplotlib",
        "plasmaboundaries",
        "uncertainties",
        "importlib_resources",
    ],
)
