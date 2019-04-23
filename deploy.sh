echo "make dist files"
python3 setup.py sdist bdist_wheel

echo "upload to pypl"
python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*