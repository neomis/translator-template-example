"""Setup Package."""
from setuptools import setup, find_packages


about = {}
with open('translator_template_example/__version__.py', 'r', encoding='utf-8') as file_handle:
    exec(file_handle.read(), about)  # pylint: disable=exec-used
    file_handle.close()

with open('README.md', 'r', encoding='utf-8') as file_handle:
    readme = file_handle.read()
    file_handle.close()

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],
    python_requires=">=3.8",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'translator_template.translators': 'example = translator_template_example.translator:main'},
    install_requires=[
        'translator-template>=1.1'
    ],
    extras_require={
        'dev': [
            'autopep8',
            'mypy',
            'pylint',
            'pytest',
            'pytest-cov',
            'twine']
    }
)
