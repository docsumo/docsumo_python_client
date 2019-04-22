# Step to create documentation

```bash

sphinx-build <file_path_which_has_conf.py_and_index.rst>  <path_to_store_docs>

# start server to check file
python -m http.server 5000

# navigate to <path_to_store_docs>

```

# Sample of docstring

```python
    """
    This is example.

    Args:
        input_dir: ``str``
            dir where protobuf are stored
        output_dir ``str``
            directory where model will be saved too
        list_lis: ``list``
            test value.

            .. code-block:: json
            
                {"this_example": "hello",
                ....}

    Returns:
        None
    """
```

# More detail
[sphnix_example](https://pythonhosted.org/an_example_pypi_project/sphinx.html)  
[sphinx_website](http://www.sphinx-doc.org/en/master/)
