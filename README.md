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

- put ``helptext`` in your INSTALLED_APPS::

    INTALLED_APPS=(
        ...
        'helptext'
        ...
    )


- if you want to insert helptext in your html pages::
.. code-block:: html

    {% load helptext %}

    {% block body %}
        {% helptext_slug 'my_slug' %}
    {% endblock body %}


- if you want to use helptext with configurated css selector::
.. code-block:: html

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


.. |master-build| image:: https://secure.travis-ci.org/marcoimme/django-helptext.png?branch=master
                    :target: http://travis-ci.org/marcoimme/django-helptext/

.. |master-cov| image:: https://coveralls.io/repos/marcoimme/django-helptext/badge.png?branch=master
                    :target: https://coveralls.io/r/marcoimme/django-helptext

.. |master-req| image:: https://requires.io/github/marcoimme/django-helptext/requirements.png?branch=master
                    :target: https://requires.io/github/marcoimme/django-helptext/requirements/?branch=master
                    :alt: Requirements Status


.. |dev-build| image:: https://secure.travis-ci.org/marcoimme/django-helptext.png?branch=develop
                  :target: http://travis-ci.org/marcoimme/django-helptext/

.. |dev-cov| image:: https://coveralls.io/repos/marcoimme/django-helptext/badge.png?branch=develop
                :target: https://coveralls.io/r/marcoimme/django-helptext

.. |dev-req| image:: https://requires.io/github/marcoimme/django-helptext/requirements.png?branch=develop
                    :target: https://requires.io/github/marcoimme/django-helptext/requirements/?branch=develop
                    :alt: Requirements Status
