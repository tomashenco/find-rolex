from setuptools import setup

setup(
    name='find-rolex',
    version="0.0.3",
    author="Tomasz Dobrzycki",
    author_email="dobrzycki.tomasz@gmail.com",
    license='BSD',
    description="Rolex finder. Console application that learns from labelled images and predicts new labels.",
    long_description=open('README.md').read(),
    url='https://github.com/tomashenco/rolex-finder',
    install_requires=['scipy>=0.17.0',
                      'numpy>=1.10.4',
                      'sklearn>=2.7.12'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Computer Vision"]
    )