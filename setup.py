from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='prettystring',
      version='0.1.1',
      description='Build ANSI color encoded strings with ease.',
      long_description=readme(),
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Terminals',
        'Topic :: Text Processing :: General',
        'Topic :: Utilities'
      ],
      keywords='color colorful pretty string strings',
      url='https://github.com/robolivable/prettystring',
      author='Robert Oliveira',
      author_email='oliveira.rlde@gmail.com',
      license='MIT',
      packages=['prettystring'],
      install_requires=['enum34==1.1.6'])
