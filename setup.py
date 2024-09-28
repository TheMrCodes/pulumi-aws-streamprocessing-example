from setuptools import setup, find_packages

setup(
    name='streamprocessing',
    version='1.0.0',
    author='Your Name',
    author_email='your@email.com',
    description='A Python package for stream processing',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'pulumi',
        'pulumi_aws',
        'python-dotenv',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)