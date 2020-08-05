import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='pyblob-logging',  
     version='0.1',
     scripts=['pyblob-logging'] ,
     author="Jorge Andrés Díaz",
     author_email="jorgeandresdn1@gmail.com",
     description="A library to log into blob storage in Azure",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/javatechy/dokr",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
