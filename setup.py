from setuptools import setup

setup(
  name='scrabble-bot',
  version='0.1',
  description='Scrabble-playing robot',
  url='https://github.com/oldironhorse/scrabble-bot',
  download_url= \
    'https://github.com/oldironhorse/scarbble-bot/archive/0.1.tar.gz',
  author='Simon Redding',
  author_email='s1m0n.r3dd1ng@gmail.com',
  license='GPL 3.0',
  packages=['scrabble','scrabble.board'],
  install_requires=[],
  test_suite='nose.collector',
  tests_require=['nose'],
  zip_safe=False)
