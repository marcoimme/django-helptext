Django Help Text
==================

.. image:: https://pypip.in/v/django-helptext/badge.png
   :target: https://crate.io/packages/django-helptext/

.. image:: https://pypip.in/d/django-helptext/badge.png
   :target: https://crate.io/packages/django-helptext/

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

    {% load helptext %}
    {% block body %}
        {% helptext_slug 'my_slug' %}
    {% endblock body %}


- if you want to use helptext with configurated css selector

    {% load helptext %}
    {% block body %}
        {% helptext  %}
    {% endblock body %}


For more informations, Docs are [here](https://django-helptext.readthedocs.org/en/latest/)!


Project links
-------------

+--------------------+----------------+--------------+-------------------------+
| Stable             | |master-build| | |master-cov| | |master-req|            |
+--------------------+----------------+--------------+-------------------------+
| Development        | |dev-build|    | |dev-cov|    | |dev-req|               |
+--------------------+----------------+--------------+-------------------------+
| Project home page: |https://github.com/marcoimme/django-helptext             |
+--------------------+---------------+-----------------------------------------+
| Issue tracker:     |https://github.com/marcoimme/django-helptext/issues?sort |
+--------------------+---------------+-----------------------------------------+
| Download:          |http://pypi.python.org/pypi/django-helptext/         |
+--------------------+---------------+-----------------------------------------+
| Documentation:     |https://django-helptext.readthedocs.org/en/latest/   |
+--------------------+---------------+--------------+--------------------------+
