from setuptools import setup, find_packages

setup(
    name='OAS_wrapper',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy<2',
        'scipy',
        'pandas',
        'matplotlib',
        'Bio'
        # Add other dependencies as needed
    ],
    author='Viswanadham Sridhara',
    author_email='Sridhara.Utils@gmail.com',
    description='The OAS_wrapper package provides functionalities to get basic statistics and visualizations for the OAS dataset of interest. In addition, the actual V/D/J sequencese are mapped from the IMGT database for a query sequence of interest.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sridhara-omics/OAS_wrapper',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)
