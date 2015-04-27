Django Help Text
==================

This is a [Django](https://www.djangoproject.com/) application to insert help text into html page

JQuery [qtip](http://qtip2.com/) plugin is used to display tooltips

How to use
----------

- put ``helptext`` in your INSTALLED_APPS
```python
    INTALLED_APPS=(
        ...
        'helptext'
        ...
    )
```

- if you want to insert helptext in your html pages
```html
    {% load helptext %}
    {% block body %}
        {% helptext_slug 'my_slug' %}
    {% endblock body %}
```

- if you want to use helptext with configurated css selector
```html
    {% load helptext %}
    {% block body %}
        {% helptext  %}
    {% endblock body %}
```

For more informations, Docs are [here](https://django-helptext.readthedocs.org/en/latest/)!


Project links
-------------
||LINKS|
|--------------------|--------------------------------------------------------|
| Project home page: |https://github.com/marcoimme/django-helptext             |
| Issue tracker:     |https://github.com/marcoimme/django-helptext/issues?sort |
| Download:          |http://pypi.python.org/pypi/django-helptext/         |
| Documentation:     |https://django-helptext.readthedocs.org/en/latest/   |
