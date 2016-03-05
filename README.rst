python-caighdean
================


Install
-------

.. code-block:: console

  $ pip install -e git+git@github.com:phlax/python-caighdean


Run
---

.. code-block:: python

   >>> from caighdean import Translator
   >>> Translator("gd").translate("foo")
   u"foo"

   >>> Translator("gv").translate("foo")
   u"foo"
