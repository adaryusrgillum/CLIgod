"""Setup script for CLIgod."""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / 'README.md'
if readme_file.exists():
    with open(readme_file, 'r', encoding='utf-8') as f:
        long_description = f.read()
else:
    long_description = 'Multi-agent content creation pipeline'

# Read requirements
requirements_file = Path(__file__).parent / 'requirements.txt'
if requirements_file.exists():
    with open(requirements_file, 'r') as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
else:
    requirements = []

setup(
    name='cligod',
    version='0.1.0',
    author='CLIgod Team',
    author_email='',
    description='Multi-agent content creation tool with Gemini, Claude, and Kimi',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/adaryusrgillum/CLIgod',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.8',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'cligod=cligod.cli:main',
        ],
    },
    include_package_data=True,
    package_data={
        'cligod': ['../config.yaml', '../.env.example'],
    },
)
