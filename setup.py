from distutils.core import setup, find_packages

setup(name='waveshare_eink',
      version='1.0',
      description='Small client and flask app which allows displaying HTML CSS marked up document on Waveshare e-ink displays',
      author='David Hutfless',
      author_email='dhvie85@gmail.com',
      packages=find_packages(),
      install_requires={
            'gunicorn'
      }
     )