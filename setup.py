
setup(name='accounting-system',
            version='0.1',
            description='todo',
            url='https://github.com/Stiliyan92/accounting-system',
            author='Stiliyan Stoyanov',
            author_email='sstoyanov@parallel.bas.bg',
            license='todo',
            packages=['accounting-system'],
            zip_safe=False)

from setuptools import setup, find_packages

setup(
    name="accounting-system",
    version="0.1",
    packages=find_packages(),
    install_requires=['configparser >= 3.5.0', 'mysqlclient >= 1.3.7',
                      'pika >= 0.10.0', 'PyMySQL >= 0.7.2'],
    author="Stiliyan Stoyanov",
    author_email="sstoyanov@parallel.bas.bg",
    description="",
    license="PSF",
    keywords="accounting system hpc grid",
    url="https://github.com/Stiliyan92"
)
