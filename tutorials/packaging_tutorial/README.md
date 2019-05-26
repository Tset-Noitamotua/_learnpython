# Packaging Tutorial

Follow the steps described in [Packaging Python Projects] tutorial on [pypi.org].

Most important commands to remember:

```bash
# setuptools and wheel is required
pip install --user --upgrade setuptools wheel

# twine is a tool used to upload packages to PyPi
pip install --user --upgrade twine
twine --version
twine --help

# MOST IMPORTANT COMMAND
# two folders will be created: build and dist
# dist will contain packages that you want to upload
python setup.py sdist bdist_wheel

# UPLOADING TO PyPi server
twine upload dist/*



# use the PyPi-test-server for tutorials and learning (requires registration)
# uploading to test server
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# installing from test server
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-your-username
python -m pip install -i https://test.pypi.org/simple/ --no-deps example-pkg-your-username
```

[Packaging Python Projects]:https://packaging.python.org/tutorials/packaging-projects/
[pypi.org]:https://pypi.org/
