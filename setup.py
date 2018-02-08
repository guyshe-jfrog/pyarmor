# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

from src.config import version
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'src', 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

pyarmor_data_files = ['pyshield.key', 'pyshield.lic', 'public.key',
                      'product.key', 'license.lic', 'README.rst',
                      'user-guide.md', 'mechanism.md',
                      'platforms/win32/_pytransform.dll',
                      'platforms/win_amd64/_pytransform.dll',
                      'platforms/linux_i386/_pytransform.so',
                      'platforms/linux_x86_64/_pytransform.so',
                      'platforms/macosx_intel/_pytransform.dylib',]

setup(
    name='pyarmor',

    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    version=version,
    description='A tool used to run or import obfuscated python scritps',
    long_description=long_description,

    url='https://github.com/dashingsoft/pyarmor',
    author='Jondy Zhao',
    author_email='jondy.zhao@gmail.com',

    # For a list of valid classifiers, see
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Utilities',

        # Pick your license as you wish
        'License :: Free To Use But Restricted',

        # Support platforms
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],

    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    #
    # Note that this is a string of words separated by whitespace, not a list.
    keywords='protect obfuscate encrypt obfuscation distribute',

    # packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    packages=['pyarmor', 'pyarmor.polyfills', 'pyarmor.webui'],
    package_dir={'pyarmor': 'src'},
    package_data={
        'pyarmor': pyarmor_data_files,
        'pyarmor.webui': ['css/*.css', 'js/*.js', '*.html', '*.js', 'manager.*'],
    },

    data_files=[
        ('docs', ['docs/user-guide.md', 'docs/rationale.md']),
    ],

    entry_points={
        'console_scripts': [
            'pyarmor=pyarmor:main',
            'pyarmor-webui=pyarmor.webui.server:main',
        ],
    },
)
