from setuptools import setup, find_packages

setup(
    name='pluxtools',
    version='0.1',
    description='Tools for PLUX image extraction and surface metric analysis',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pillow',
        'opencv-python-headless',
        'pandas',
        'scikit-image',
        'scipy',
        'tqdm',
    ],
    python_requires='>=3.7',
)
