package:
	python3 setup.py sdist
upload: package
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
