Install
========
   .. code-block:: bash

        pip install docsumo

Docsumo Examples
================

.. code-block:: python

    from docsumo import Docsumo

    docsumo = Docsumo()
    print(docsumo.user_detail_credit_limit())
    print("====================================")
    print(docsumo.documents_summary())

Output

.. code-block:: json 

    {'error': '',
    'error_code': '',
    'message': '',
    'status': 'success',
    'status_code': 200,
    'data': {'email': 't@docsumo.com',
            'full_name': 'Docsumo Tester',
            'monthly_doc_current': 75,
            'monthly_doc_limit': 300,
            'user_id': '5cb45f1f5a8'}
    }

    ====================================

    {
        "data": {
                "all": 6,
                "processed": 0,
                "review": 5,
                "skipped": 0
        },
        "error": "",
        "error_code": "",
        "message": "",
        "status": "success",
        "status_code": 200
    }

   