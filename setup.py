from setuptools import find_packages, setup
with open('docs/quickstart.rst', 'r') as f:
    QUICKSTART = f.read()


setup(
    name='django-fabric',
    version='1.5.3',
    author='Rolf Erik Lekang',
    author_email='rolf@mocco.no',
    url='http://mocco.no/django-fabric/',
    packages=find_packages(),
    description='a generic fabric utility class for django projects',
    long_description=QUICKSTART,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    include_package_data=True,
    test_suite='tests.run',
    zip_safe=False,
    install_requires=['fabric', 'django', 'requests'],
    test_requires=['fabric', 'django', 'requests'],
    entry_points={
        'console_scripts': [
            'django-fabric-init = django_fabric.commands:init',
        ]
    }
)
