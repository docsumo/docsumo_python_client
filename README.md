# Welcome to Docsumo python client documentation!
[![Documentation Status](https://readthedocs.org/projects/docsumo/badge/?version=latest)](https://docsumo.readthedocs.io/en/latest/?badge=latest)

For detail:
- [Here is Documentation](https://docsumo.readthedocs.io/en/latest/index.html)  
- [Postman Documentation](https://documenter.getpostman.com/view/4263853/S11LtdGN)


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
# OR
# doc = Docsumo(apikey="fghhGh56HHJ...")

# To get the user detail & credit limit.
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