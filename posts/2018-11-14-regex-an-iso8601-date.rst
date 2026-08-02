.. title: Using regex to filter an ISO8601 date
.. slug: 2018-11-14-regex-an-iso8601-date
.. date: 2018-11-14 09:36:57
.. type: text
.. tags: sciblog

It can be useful to find a pattern such an ISO8601-formatted date in a set of files.
I discovered it is possible to do that in the `atom <https://atom.io/>`_  editor:

.. image:: ../files/2018-11-14-regex-an-iso8601-date.png

.. TEASER_END

- simply use that code to find the YYYY-MM-DD part:

    ::

        (\d{4})-(\d{2})-(\d{2})
