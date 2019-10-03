all: dotest

dotest:
	./pyastsim test/copied/*.py || echo "Test 1 Passed"
	./pyastsim --threshold 100 test/copied/*.py && echo "Test 2 Passed"