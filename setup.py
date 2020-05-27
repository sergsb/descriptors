import setuptools

__version__ = "0.0.1"
    
setuptools.setup(
    name="descriptors",
    version=__version__,
    author="S.Sosnin",
    author_email="sergey.sosnin@skoltech.ru",
    description="Chemical descriptors",
    url="http://github.com/sergsb/descriptors",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'mordred',
          'e3fp'
    ],
    python_requires='>=3.6',
)
