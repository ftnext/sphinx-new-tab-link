.. _japanese_guide:

``sphinx-new-tab-link`` 使い方ガイド
=============================================================

| ``sphinx-new-tab-link`` はSphinx拡張です。
| ソースからビルドしたHTMLで、 **外部リンクをブラウザの新しいタブで開く** ように自動で設定します✨
| このドキュメントで使い方を示します（なんと、このドキュメントはドッグフーディングにもなっているんですよ！🐶）

*Here is English version of this guide:* :ref:`english_guide`

リンク集
--------------------

* PyPI https://pypi.org/project/sphinx-new-tab-link/
* `GitHub Repository <https://github.com/ftnext/sphinx-new-tab-link>`_

インストール
--------------------

``sphinx-new-tab-link`` はPyPIからインストールできます。

.. code-block:: shell

    $ pip install sphinx-new-tab-link

使い方
--------------------

あなたのSphinxプロジェクトの :file:`conf.py` でこの拡張を有効にしてください。

.. code-block:: python
    :caption: conf.py

    extensions = [
        "sphinx_new_tab_link",
    ]

これだけです！

HTML中の外部リンクが、ブラウザの新しいタブで開かれるようになります。

対応している記法
--------------------

reSTで可能なさまざまな記法による外部リンクをサポートしています。

✅直接URLだけを書いた行

https://github.com/ftnext/sphinx-new-tab-link

✅インラインで書いたURL（「リンク集」の *PyPI* 参照）

.. _公開版ガイド: https://ftnext.github.io/sphinx-new-tab-link/guide.html

✅外部ハイパーリンクターゲットを定義し、それを参照： `公開版ガイド`_

.. code-block:: rest

    .. _公開版ガイド: https://ftnext.github.io/sphinx-new-tab-link/guide.html

    外部ハイパーリンクターゲットを定義し、それを参照： `公開版ガイド`_

.. __: https://ftnext.github.io/sphinx-new-tab-link/guide.html

✅匿名ハイパーリンク記法： `公開版ガイド（匿名記法）`__

.. code-block:: rest

    .. __: https://ftnext.github.io/sphinx-new-tab-link/guide.html

    匿名ハイパーリンク記法： `公開版ガイド（匿名記法）`__

✅アンダースコア2つの埋め込みURL： `GitHub Repository（ターゲット定義なし） <https://github.com/ftnext/sphinx-new-tab-link>`__

.. code-block:: rst

    `GitHub Repository（ターゲット定義なし） <https://github.com/ftnext/sphinx-new-tab-link>`__

✅アンダースコア1つの埋め込みURLによって定義したターゲット（リンク集の *GitHub Repository*）を再度参照： `GitHub Repository`_

.. code-block:: rst

    `GitHub Repository <https://github.com/ftnext/sphinx-new-tab-link>`_

    再度 `GitHub Repository`_ を参照できる

✅ ``:target:`` オプションを指定した ``image`` ディレクティブ

.. image:: _static/breakfast.jpg
    :target: https://www.flickr.com/photos/pyconjp/48818171768/in/album-72157710870622516/

.. code-block:: rst

    .. image:: _static/breakfast.jpg
        :target: https://www.flickr.com/photos/pyconjp/48818171768/in/album-72157710870622516/

✅ ``:target:`` オプションを指定した ``figure`` ディレクティブ

.. figure:: _static/pyconjp2019.jpg
    :target: https://www.flickr.com/photos/pyconjp/48743997848/in/album-72157710870622516/

.. code-block:: rst

    .. figure:: _static/pyconjp2019.jpg
        :target: https://www.flickr.com/photos/pyconjp/48743997848/in/album-72157710870622516/

.. note:: `sphinx.ext.autodoc <https://www.sphinx-doc.org/ja/master/usage/extensions/autodoc.html>`__ にも対応しています！

    URLを含んだdocstringからビルドしたHTMLでも、URLはブラウザの新しいタブで開きます。
    ``sphinx-new-tab-link`` の :doc:`api` のドキュメントは、その例になっているんですよ！🐶

Enjoy documentation!🙌
