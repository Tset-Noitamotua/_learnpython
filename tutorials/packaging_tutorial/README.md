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

# UPLOADING TO PyPi server (requires registration)
twine upload dist/*
# alternatively
python -m twine upload dist/*
# you will be prompted for pypi-username and password



# use the PyPi-test-server for tutorials and learning (requires registration)
# uploading to test server
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# installing from test server
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-your-username
python -m pip install -i https://test.pypi.org/simple/ --no-deps example-pkg-your-username
```

For more details check setuptools documentation for [Packaging and distributing projects].

[Packaging Python Projects]:https://packaging.python.org/tutorials/packaging-projects/
[pypi.org]:https://pypi.org/
[Packaging and distributing projects]:https://packaging.python.org/guides/distributing-packages-using-setuptools/#packaging-and-distributing-projects
