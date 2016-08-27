from setuptools import setup, find_packages

setup(
    name="accounting-system",
    version="0.1",
    packages=find_packages(exclude=['tests']),
    install_requires=['configparser >= 3.5.0', 'mysqlclient >= 1.3.7',
                      'pika >= 0.10.0', 'PyMySQL >= 0.7.2',
                      'mysqlclient >= 1.3.7'],
    author="Stiliyan Stoyanov",
    author_email="sstoyanov@parallel.bas.bg",
    description="",
        classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Scientigic users',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords="accounting system hpc grid",
    url="https://github.com/Stiliyan92"
    package_data={
        'accouting-system': ['pbs_log', 'tests/example.conf',
         tests/pbs_test_log],
        },
)
