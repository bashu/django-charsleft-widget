import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-charsleft-widget',
    version='0.1',
    packages=['charsleft_widget'],
    include_package_data=True,
    license='BSD License',
    description='Put short description here...',
    long_description=README,
    url='http://github.com/bashu/django-charsleft-widget',
    author='Basil Shubin',
    author_email='basil.shubin@gmail.com',
    install_requires=[
        'jinja2==2.7.1',
        'django-jinja==0.21',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    zip_safe=False,
)
