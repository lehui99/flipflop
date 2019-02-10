# Bootstrap setuptools

from distutils.core import setup

setup(
    name='flipflop',
    version='1.0.1',
    py_modules=['flipflop'],
    provides=['flipflop'],
    author='lehui99',
    author_email='lehui99@gmail.com',
    description='FastCGI wrapper for WSGI applications',
    url='https://github.com/lehui99/flipflop',
    license='BSD',
    classifiers=[
        "Development Status :: 4 - Beta",
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
