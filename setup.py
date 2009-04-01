from distutils.core import setup
import os

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

# snippet from http://django-registration.googlecode.com/svn/trunk/setup.py
for dirpath, dirnames, filenames in os.walk('django_css'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[11:] # Strip "registration/" or "registration\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))
setup(
    name='django-css',
    version='1.0.0',
    description='django-css provides an easy way to use CSS compilers with Django projects, and an automated system for compressing CSS and JavaScript files',
    author='David Ziegler',
    author_email='David Ziegler <davdi.ziegler@gmail.com>',
    url='http://code.google.com/p/django-css/',
    packages = packages,
    package_data = {'django_css': data_files,},
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ]
)
