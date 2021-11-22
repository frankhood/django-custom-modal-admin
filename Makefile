upgrade-requirements:
	pip install -q -U pip pip-tools setuptools
	pip-compile -q -U -o requirements_dev.txt requirements_dev.in 
	pip-compile -q -U -o requirements_test.txt requirements_test.in
	echo "!!!!!! 🚨 REMOVE Django from requirements_test.txt for tox testing 🚨 !!!!!!" 