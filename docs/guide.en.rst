.. _english_guide:

Guide of ``sphinx-new-tab-link``
=============================================================

| ``sphinx-new-tab-link`` is a Sphinx extension.
| It builds HTML from source which enables **your browser to open external links in new tabs** ✨
| I'll show you how to use it in this document (oh my gosh, this document is dogfooding too! 🐶)

*このガイドの日本語版はこちらにあります：* :ref:`japanese_guide`

Links
--------------------

* PyPI https://pypi.org/project/sphinx-new-tab-link/
* `GitHub Repository <https://github.com/ftnext/sphinx-new-tab-link>`_

Installation
--------------------

You can install ``sphinx-new-tab-link`` from PyPI.

.. code-block:: shell

    $ pip install sphinx-new-tab-link

How to use
--------------------

Enable this extension in your Sphinx project's :file:`conf.py`.

.. code-block:: python
    :caption: conf.py

    extensions = [
        "sphinx_new_tab_link",
    ]

That's it!

External links in HTML will be opened in a new tab of the browser.

Enjoy documentation!🙌
