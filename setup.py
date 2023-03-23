from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="docsumo",
    version="0.5.9",
    description="Python client for Docsumo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.docsumo.com/",
    author="Docsumo",
    author_email="hello@docsumo.com",
    license="MIT",
    python_requires=">=3",
    packages=["docsumo"],
    install_requires=["requests"],
    classifiers=[
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
    ],
    zip_safe=False,
)
