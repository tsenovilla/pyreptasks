import setuptools
from git_setups import versioneer

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("git_setups/requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setuptools.setup(
    name="pyreptasks",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url="https://github.com/tsenovilla/pyreptasks",
    author="Tomás Senovilla Polo",
    author_email="tspscgs@gmail.com",
    description="This Python library provides the user with some tools useful to automate coding of repetitive tasks",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    packages=setuptools.find_packages(),
    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
)
