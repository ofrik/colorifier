import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='colorifier',
    version='1.3',
    author="Ofri Masad",
    author_email="ofrik89@gmail.com",
    description="Classifier for colors",
    url="https://github.com/ofrik/colorifier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    package_data={'colorifier': ["colorifier/model.pkl"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
