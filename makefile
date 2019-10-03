all: dotest

script=pyastsim/pyastsim

dotest:
	$(script) test/copied/*.py || echo "Test 1 Passed"
	$(script) --threshold 100 test/copied/*.py && echo "Test 2 Passed"