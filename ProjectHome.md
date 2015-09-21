### This project has joined the exodus and moved to github. ###

New link: http://github.com/dziegler/django-css/tree/master

You should go there for future updates and to download the source

# What is django-css? #
Django-css is a fork of [django\_compressor](http://github.com/mintchaos/django_compressor/tree/master) that makes it easy to use CSS compilers with your Django projects. CSS compilers extend CSS syntax to include more powerful features such as variables and nested blocks, and pretty much [rock](http://blog.davidziegler.net/post/92203003/css-compilers-rock) all around. Django-css can currently be used with any CSS compiler that can be called from the command line, such as [HSS](http://ncannasse.fr/projects/hss), [Sass](http://haml.hamptoncatlin.com/docs/rdoc/classes/Sass.html), [CleverCSS](http://github.com/dziegler/clevercss/tree/master), or [LESS](http://lesscss.org/).

Thanks to django\_compressor, django-css will also version and compress linked and inline javascript or CSS into a single cached static file.

Note: The pypi version of CleverCSS is buggy and will not work with django-css. Use the updated version on github: http://github.com/dziegler/clevercss/tree/master

# 6/7/09 - Version 2 is here! What's new? #
Django-css was previously using django-compress for versioning and compression, and it now uses django\_compressor. The main reasons being that with django\_compressor, css/js files are included in the template itself, not in settings, and versioning is much cleaner. Version 2 requires much less setup and is easier to use, but is not compatible with version 1.

Special thanks to Christian Metts and Andreas Pelme for all their hard work on django\_compressor and django-compress.