import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="samfilt", # Replace with your own username
    version="0.0.1",
    author="Alec Bahcheli",
    author_email="abahchel@uwo.ca",
    description="Sam file filtering script.",
    long_description=long_description,
    long_description_content_type="sam file",
    url="https://github.com/abahcheli/samfilt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Academic Free License version 3.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)