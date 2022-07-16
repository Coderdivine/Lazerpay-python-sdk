from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='LazerPayFinance',
  version='0.0.1',
  description='A Simplified way to use LazerPayFinance api',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Ezechukwu Chimdi',
  author_email='chimdi4332@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Lazerpay', 
  packages=find_packages(),
  install_requires=['requests','web3']
)