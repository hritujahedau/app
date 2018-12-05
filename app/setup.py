from setuptools import setup, find_packages

try:
    with open('requirements.txt') as f:
        requires = f.read().splitlines()
except IOError:
    with open('agroutils.egg-info/requires.txt') as f:
        requires = f.read().splitlines()

with open('VERSION') as f:
    version = f.read().strip()

print requires
print type(requires)

setup(
      # If name is changed be sure to update the open file path above.
      name = "agroutils",
      version = version,
      packages = find_packages(),
      package_dir = {'agroutils':'agroutils'},
      author = 'AgroStar',
      author_email = 'technology@agrostar.in',
      descipriton = 'Utility functions repo used across AgroStar',
      license = "PSF",
      include_package_data = True,
      )
