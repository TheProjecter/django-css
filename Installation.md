# This information is for Version 1 and is deprecated. #
### New users are encouraged to use Version 2  found on github: http://github.com/dziegler/django-css/tree/master ###


# Installing django-css #

  1. Checkout from svn: ` svn co http://django-css.googlecode.com/svn/trunk/ django-css `
  1. Install with setup.py: ` python setup.py install ` or manually add the django-css directory to your PYTHONPATH
  1. Add 'django-css' to your INSTALLED\_APPS

django-css does not create any models, so you don't need to sync the database.

# Installing the CSS compiler #
You will need to choose a CSS compiler to use. Some popular ones are:
  * HSS - http://ncannasse.fr/projects/hss
  * Sass - http://haml.hamptoncatlin.com/docs/rdoc/classes/Sass.html
  * CleverCSS - ~~http://sandbox.pocoo.org/clevercss~~.  There are bugs in the pypi version of CleverCSS that will cause it to fail with django-css. Use the most recent patched version found here: http://github.com/dziegler/clevercss/tree/master

I wrote a blog post [here](http://blog.davidziegler.net/post/92203003/css-compilers-rock) discussing CSS compilers. Personally, I prefer CleverCSS because I like its features and pythonic syntax.

# Installing a CSS and/or JS compressor #

You will need to install a CSS and/or Javascript compressor. The current options are:
  * CSSTidy - Compresses CSS - http://csstidy.sourceforge.net/
  * YUICompressor - Compresses CSS and JS - http://www.julienlecomte.net/yuicompressor/
  * JSMin -  Compresses JS - Included with installation

By default django-css and django-compress use CSSTidy to compress CSS. If you do not install CSSTidy, make sure to disable the filter in your settings by setting COMPRESS\_CSS\_FILTERS = None.

See the [Usage](http://code.google.com/p/django-css/wiki/Usage) page for setting up and using django-css.
