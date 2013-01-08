Cardinal Web Dev
================

Auto-generated from [Kevin Xu](https://github.com/imkevinxu)'s [Django Project Builder](https://github.com/imkevinxu/django-projectbuilder)

### Team

* Kevin Xu <kevin@imkevinxu.com>
* Charlie Guo <charlierguo@gmail.com>
* Kingston Tam <ktam@stanford.edu>

## Getting Started

### Dependencies

For best results, make sure you have at least:

* Python 2.7.2
* Django 1.4.1

### Customizations

* [Jinja2](http://jinja.pocoo.org/docs/) templating with [Coffin](https://github.com/coffin/coffin)
* [Django Debug Toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar)
* [bcrypt](https://docs.djangoproject.com/en/dev/topics/auth/#using-bcrypt-with-django) password hashing
* [South](http://south.readthedocs.org/en/0.7.6/index.html) database migration

### Installing the Application

    # after initial git clone of existing repo
    cd cardinalwebdev/
    mkvirtualenv cardinalwebdev                                       # requires proper virtualenv setup
    workon cardinalwebdev                                             # sets the virtual environment

    pip install -r requirements.txt                                   # installs all python packages
    python manage.py syncdb                                           # sets up django database
    python manage.py migrate cardinalwebdev_app                       # migrates any south migrations

## Troubleshooting

### Workflow

In case something's not working after pulling, try one of these:

    workon cardinalwebdev                                             # make sure you're in the right virtual environment
    pip install -r requirements.txt                                   # make sure python packages are up to date
    python manage.py migrate cardinalwebdev_app                       # make sure database schema is migrated

### Missing Dependencies

If you are missing some dependencies like `pip`, `django`, `virtualenv`, or`virtualenvwrapper`
then try downloading and running this [script](https://github.com/imkevinxu/django-projectbuilder/blob/master/install_dependencies.sh) or use this line of code:

    curl -O https://raw.github.com/imkevinxu/django-projectbuilder/master/install_dependencies.sh && source install_dependencies.sh && rm -f install_dependencies.sh

Script has been tested with Mac OSX 10.7 (Lion) and 10.8 (Mountain Lion) so far.