import setuptools
from shutil import rmtree

setuptools.setup( 
    name='Todo-CLI', 
    version='1.0', 
    author='Advait Jadhav', 
    description='A basic Todo application that works on CRUD operations. Fueled by PyInquirer, rich and click for CLI.', 
    packages=setuptools.find_packages(), 
    entry_points={ 
        'console_scripts': [ 
            'todo = TodoApp.__main__:main' 
        ] 
    }, 
    classifiers=[ 
        'Programming Language :: Python :: 3', 
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent', 
    ], 
)

dirs = ["build", "dist", "Todo_CLI.egg-info"]

for dir in dirs:
	rmtree(dir)