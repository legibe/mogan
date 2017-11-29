from setuptools import setup

setup(name='zuolib',
      version='0.1',
      description='Wrapper Zuora API wrapper with goodies',
      url='http://github.com/legibe/zuolib',
      author='Claude Gibert',
      author_email='claude.gibert@gmail.com',
      license='MIT',
      packages=['zuolib'],
      zip_safe=False,
      install_requires=[
          'PyYAML',
          'requests'
      ],
      test_suite='nose.collector',
      test_requires=['nose']
)
