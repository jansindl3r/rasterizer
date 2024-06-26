from setuptools import setup, find_packages

setup(
    name='rasterizer',
    version='0.1',
    packages=find_packages(),
    description='no design foundry – rasterizer plugin',
    author='Jan Sindler',
    author_email='jansindl3r@example.com',
    package_data={'': ['aglfn.txt']},  # Include aglfn.txt in all packages
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    keywords='rasterizer, plugin',
    python_requires='>=3.6',
)