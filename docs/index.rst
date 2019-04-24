.. email documentation master file, created by
   sphinx-quickstart on Thu Aug  9 13:47:11 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Docsumo python client documentation!
===============================================

Install
========
    .. code-block:: bash

        pip install docsumo

Available method
================
    .. code-block:: bash

        doc.user_detail_credit_limit()
        doc.documents_list()
        doc.documents_summary()
        doc.upload_file(
                "./data/invoice.pdf",
                "invoice",
            )
        )
        doc.extracted_data("c511ba245484442fb")

Example
=======

.. toctree::
   :maxdepth: 2

   welcome


Docsumo Class
=============

.. toctree::
   :maxdepth: 2

   docsumo


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
