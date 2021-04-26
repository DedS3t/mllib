 
from setuptools import setup

setup(
    name='mllib',
    version='0.1.0',    
    description='The ML library',
    author='Dennis Zax',
    author_email='denniszax32@gmail.com',
    license='mit',
    packages=['mllib.metrics', 'mllib.models', 'mllib.helpers'],
    install_requires=['pandas',
                      'numpy',
                      ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: ezml users',
        'License :: mit License',  
        'Operating System :: any',        
        'Programming Language :: Python :: >3',
    ],
)