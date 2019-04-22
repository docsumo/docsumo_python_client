# Welcome to utilspy documentation!
[![Documentation Status](https://readthedocs.org/projects/utilpy/badge/?version=latest)](https://utilpy.readthedocs.io/en/latest/?badge=latest)

Docsumo.

For detail [Here is Documentation](https://utilpy.readthedocs.io/en/latest/index.html)

# Install 
```bash
pip3 install docsumo
```

# set API KEY from docsumo Setting page as env variable
```bash
export DOCSUMO_APi_KEY="test" >>  ~/.bashrc
source ~/.bashrc
```


# Example
``` py
from docsumo import Docsumo

doc = Docsumo()

# To get the user detail and user credit linit information
print(doc.limit())
```

Output:
```
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