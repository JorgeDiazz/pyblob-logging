import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='pyblob_logging',  
     version='0.1.0	',
     scripts=['pyblob_logging'] ,
     author="Jorge Andres Diaz",
     author_email="jorgeandresdn1@gmail.com",
     description="A library to log into blob storage in Azure",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/JorgeDiazz/pyblob-logging",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
