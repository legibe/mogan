from setuptools import setup, find_packages

packages = find_packages(where='.')
print(packages)
setup(
      name='mogan',
      packages=packages,
      version='0.1',
      description='Utilities',
      url='http://github.com/legibe/mogan',
      author='Claude Gibert',
      author_email='claude.gibert@gmail.com',
      license='MIT',
      install_requires=[
          'PyYAML',
      ]
)
