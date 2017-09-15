from setuptools import setup, find_packages


classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Software Development :: Libraries',
]

setup(
    name='falcon-json-middleware',
    author='Jordan Ambra',
    author_email='jordan@serenitysoftware.io',
    url='https://github.com/boomletsgo/falcon-json-middleware',
    version='0.3.1',
    classifiers=classifiers,
    description='Falcon middleware to serialize and deserialize JSON requests and responses',
    keywords='falcon json middleware',
    packages=["falcon_json_middleware"],
    install_requires=["falcon>=1.0.0"],
    include_package_data=True,
    license='The Unlicense',
)
