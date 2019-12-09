from setuptools import setup, find_namespace_packages

requirements = ['scikit-learn==0.20.0', 'numpy',
                'dependency-injector', 'pika', 'click', 'pandas']

setup(name='bayes',
      version='0.1.0',
      packages=find_namespace_packages(where='src'),
      package_dir={'': 'src'},
      install_requires=requirements,
      entry_points={
          'console_scripts': [
              'bayes=bayes.command.__main__:cli'
          ]
      })
