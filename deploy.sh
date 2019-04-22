echo "make dist files"
python3 setup.py sdist bdist_wheel

echo "upload to pypl"
twine upload dist/*