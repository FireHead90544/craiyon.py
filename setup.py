from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    readme = fh.read()

setup(name='craiyon.py',
      version='0.1.0',
      description='API Wrapper for craiyon.com (DAL-E-MINI). Generate awesome images from text tokens.',
      long_description=readme,
      long_description_content_type="text/markdown",
      url='https://github.com/FireHead90544/craiyon.py',
      project_urls={
        "Issue tracker": "https://github.com/FireHead90544/craiyon.py/issues",
      },
      author='Rudransh Joshi',
      author_email='rudranshjoshi1806@gmail.com',
      platforms='any',
      license='Apache License 2.0',
      packages=['craiyon'],
      zip_safe=False,
      install_requires=["requests"])