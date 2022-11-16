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

Enjoy documentation!🙌
