from setuptools import setup
import re


with open('README.md') as f:
    long_description = f.read()

with open('LMQL/version.py', 'r', encoding='utf-8') as f:
    version = re.search(r"^__version__\s*=\s*'(.*)'.*$", f.read(), flags=re.MULTILINE).group(1)

setup(
    name='LMQL',
    version=version,
    packages=['LMQL'],
    description='Lightweight Message Queue Library',
    long_description=long_description,
    author='Misam saki',
    author_email='misamplus@gmail.com',
    url='https://gitlab.ygraphy.ir/misam/LMQ',
    install_requires=['requests'],
    license='Proprietary',
    classifiers=[
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Development',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers'
    ]
)
