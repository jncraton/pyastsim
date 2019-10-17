all: dotest

script=python3 pyastsim/pyastsim.py

dotest:
	$(script) test/copied/*.py || echo "Test 1 Passed"
	$(script) --threshold 100 test/copied/*.py && echo "Test 2 Passed"
	$(script) test/copied-c/*.c || echo "Test 3 Passed"

upload:
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*

clean:
	rm -rf pyastsim.egg-info
	rm -rf pyastsim/__pycache__
	rm -rf dist
	rm -rf build
