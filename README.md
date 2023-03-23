
# Welcome to Docsumo python client documentation!
[![Documentation Status](https://readthedocs.org/projects/docsumo/badge/?version=latest)](https://docsumo.readthedocs.io/en/latest/?badge=latest)

Check us out at [https://www.docsumo.com/](https://www.docsumo.com/)  
To find out about our web app or to get your API key, check out [https://app.docsumo.com/](https://app.docsumo.com/)

- [Here is Documentation](https://docsumo.readthedocs.io/en/latest/index.html)  
- [Postman Documentation](https://documenter.getpostman.com/view/4263853/S11LtdGN)

# Install 
```bash
pip3 install docsumo
```

# Set API KEY from docsumo setting page as env variable `DOCSUMO_API_KEY` or pass apikey parameter in Docsumo class.

![APIKeY](https://i.imgur.com/hDCh6cU.png)

```bash
export DOCSUMO_API_KEY="test" >>  ~/.bashrc
source ~/.bashrc
```


# Example
``` py
from docsumo import Docsumo

doc = Docsumo()
# OR
# doc = Docsumo(apikey="fghhGh56HHJ...")

# available method
doc.user_detail_credit_limit()
doc.documents_list()
doc.documents_summary()
doc.upload_file(
        "./data/invoice.pdf",
        "invoice",
    )
)
doc.extracted_data("c511ba245484442fb")

```

Output:
```
# To get the user detail & credit limit.
print(doc.user_detail_credit_limit())

{'error': '',
 'error_code': '',
 'message': '',
 'status': 'success',
 'status_code': 200,
 'data': {'email': 'tester@docsumo.com',
          'full_name': 'Docsumo Tester',
          'monthly_doc_current': 75,
          'monthly_doc_limit': 300,
          'user_id': '5cb45f1f5a841101f703770a'}}
```
____