from distutils.core import setup

required_pkgs = [
    "pandas",
    "numpy"
]

setup (
    name='restrack',
    version='0.0.1',
    packages=['restrack'],
    install_requires=required_pkgs,
    entry_points={
        'console_scripts': ['restrack=restrack.main:main']
    }
)