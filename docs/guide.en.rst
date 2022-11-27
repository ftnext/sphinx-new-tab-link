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

Supported notations
--------------------

It supports various notations of a external link possible in reST.

✅Line with URL only

https://github.com/ftnext/sphinx-new-tab-link

✅URL written inline (See *PyPI* at 'Links' section)

.. _Published guide: https://ftnext.github.io/sphinx-new-tab-link/guide.html

✅Define an external hyperlink target and refer it: `Published guide`_

.. code-block:: rest

    .. _Published guide: https://ftnext.github.io/sphinx-new-tab-link/guide.html

    Define an external hyperlink target and refer it: `Published guide`_

.. __: https://ftnext.github.io/sphinx-new-tab-link/guide.html

✅Anonymous hyperlink notation: `published guide (anonymous notation)`__

.. code-block:: rest

    .. __: https://ftnext.github.io/sphinx-new-tab-link/guide.html

    Anonymous hyperlink notation: `published guide (anonymous notation)`__

✅Embedded URL with double underscore: `GitHub Repository (without target definition) <https://github.com/ftnext/sphinx-new-tab-link>`__

.. code-block:: rst

    `GitHub Repository (without target definition) <https://github.com/ftnext/sphinx-new-tab-link>`__

✅Refer again to the target defined by the embedded URL with single underscore (See *GitHub Repository* at 'Links' section): `GitHub Repository`_

.. code-block:: rst

    `GitHub Repository <https://github.com/ftnext/sphinx-new-tab-link>`_

    Can refer `GitHub Repository`_ again.

.. note:: note: Also supports `sphinx.ext.autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`__!

    For HTML built from a docstring containing a URL, your browser open the URL in a new tab.
    The :doc:`api` documentation of ``sphinx-new-tab-link`` is an example of that! 🐶

Enjoy documentation!🙌
