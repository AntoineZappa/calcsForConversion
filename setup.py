import setuptools



if __name__ == "__main__":
    
    with open("README.md", "r") as fh:
        long_description = fh.read()

    setuptools.setup(
        name="converters",  # Replace with your own username
        version="0.0.1",
        author="Antonio G.B.",
        author_email="author@example.com",
        description="A small converter",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/AntoineZappa/calcsForConversion",
        packages=['converters'], # to find automatically setuptools.find_packages()
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.8.5',
    )

# to install project modules use pip install -r requirements.txt

