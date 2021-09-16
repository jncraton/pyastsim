import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyastsim",
    version="1.2.0",
    author="Jon Craton",
    author_email="jon@joncraton.com",
    description="Detect similarities between Python source files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jncraton/pyastsim",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'pyastsim=pyastsim:main',
        ],
    },
    install_requires=[
        'astunparse',
        'editdistance',
    ],
)