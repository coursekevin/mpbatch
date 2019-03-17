import setuptools

with open("README.md","r") as fh:
	long_description = fh.read()

setuptools.setup(
	name = "mpbatch",
	version = "0.1",
	author ="Kevin Course",
	author_email = "kevin.course@mail.utoronto.ca",
	description="Easy multi-core processing of batch-type processes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/coursekevin/avlpy",
    install_requires=['multiprocessing'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
)