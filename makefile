all: dotest

script=pyastsim/pyastsim

dotest:
	$(script) test/copied/*.py || echo "Test 1 Passed"
	$(script) --threshold 100 test/copied/*.py && echo "Test 2 Passed"

upload:
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*

clean:
	rm -rf pyastsim.egg-info
	rm -rf dist
	rm -rf build
