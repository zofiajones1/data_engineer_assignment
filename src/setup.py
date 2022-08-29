import os
from codecs import open as codecs_open
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))


setup(
    name="analytics_database",
    version="0.0.1",
    # The project's main homepage.
    url="https://github.com/salimfadhley/data_engineer_assignment",
    # Author details
    author="Zofia Jones",
    author_email="zofia.jones@gmail.com",
    # Choose your license
    license="All Rights Reserved",
    package_dir={"": "main"},
    entry_points={"console_scripts": ["db_import=assignment.main:main"]},
    install_requires=[
        "sqlalchemy==1.4.40",
        "beautifulsoup4",
        "requests",
        "psycopg2-binary",
	"random2==1.0.1",
	"opencv-python==4.6.0.66",
	"scikit-image==0.19.3",
	"python-dotenv==0.20.0",
        "wheel==0.37.1",
        "pyyaml==6.0",
    ],
    tests_require=[
        "pytest",
    ],
    test_suite="tests/test_assignment/example_test.py"
)
