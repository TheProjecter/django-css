# This information is for Version 1 and is deprecated. #
### New users are encouraged to use Version 2  found on github: http://github.com/dziegler/django-css/tree/master ###

# Configuration and Usage #

Configuration and usage of django-css is almost identical to django-compress. See the [Configuration](http://code.google.com/p/django-compress/wiki/Configuration) and [Usage](http://code.google.com/p/django-compress/wiki/Usage) pages at django-compress for information on configuring and usage.

CSS files will still be treated as CSS files, but you can also use HSS, Sass, or whatever other compiler format you want. For example, to include the HSS file base.hss:

```
COMPRESS_CSS = {
    'css': {
	'source_filenames': ('reset.css','base.hss','css/ie_specific.hss'),
	'output_filename': 'all_compressed.r?.css'
    }
}
```
Remember that these files are assumed to be relative to MEDIA\_ROOT.


django-css will select which CSS compiler to use based off a file's extension. Adding the following to your settings.py,

```
COMPILER_FORMATS = {
        '.sass': {
            'binary_path':'sass',
            'arguments': 'SOURCE_FILENAME.sass SOURCE_FILENAME.css' 
        },
        '.hss': {
            'binary_path':'/home/dziegler/hss',
            'arguments':'SOURCE_FILENAME.hss'
        }
    }
```

will use Sass to compile `*.sass` files, and HSS to compile `*.hss` files.

`binary_path` is the path to the CSS compiler. In the above example, sass is installed in my path, and hss is located at /home/dziegler/hss.

`arguments` are arguments you would call in the command line to the compiler. The order and format of these will depend on the CSS compiler you use. Prior to compilation, `SOURCE_FILENAME` will be replaced with the name of your file to be compiled, for example `reset`, `base`, or `css/ie_specific`.

If this seems a little hacky, it's because it is. django-css was written this way to make it easy to use whatever CSS compiler you want with as little setup as possible.

# Deployment #
In a production environment you probably don't want your source files to be evaluated and
regenerated (if needed) on every request. Adding the following to settings.py will cause django-css to assume that all CSS and JS files have been compiled and compressed.
```
COMPRESS_AUTO = False
COMPRESS_VERSION = True
```
If the above settings are not included in settings.py, django-css will automatically recompile and regenerate the CSS/JS files on every request, which is obviously not recommended during deployment.