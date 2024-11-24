from setuptools import setup, find_packages

setup(
    name='OAS_wrapper',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'pandas',
        'matplotlib',
        'Bio'
        # Add other dependencies as needed
    ],
    author='Viswanadham Sridhara',
    author_email='Sridhara.Utils@gmail.com',
    description='Python package to parse Observed antibody sequence data for easy reporting, visualization, annotation and alignment.',
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
