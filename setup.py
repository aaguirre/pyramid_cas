import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
        'pyramid',
        'SQLAlchemy',
        'transaction',
        'pyramid_tm',
        'pyramid_debugtoolbar',
        'zope.sqlalchemy',
    ]

setup(name='pyramid_cas',
      version='0.2 alpha',
      description='pyramid_cas',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Alvaro Aguirre',
      author_email='alvaro.aguirre.o@gmail.com',
      url='http://www.kundart.com',
      keywords='web pyramid pylons cas authentication',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="pyramid_cas",
      entry_points = """\
      [paste.app_factory]
      main = pyramid_cas:main
      """,
      paster_plugins=['pyramid'],
      )

