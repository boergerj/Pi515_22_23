# Unit Testing in Python

* What is unit-testing?
* Why do unit-testing?
* When to run unit-tests?

# How to add unit tests?

## Quick tour of `Calculator`

## Built-in `unittest` module (PyUnit)
* https://docs.python.org/3/library/unittest.html
* No extra dependencies.
* Standard convention.
* Rather verbose.

```
> python unittest_calculator.py
```

## `pytest` package (PyTest)
* https://docs.pytest.org/en/7.2.x/
  * `pip install pytest`
* Great plugin supports.
* Simpler syntax.

```
> python test_calculator.py
```

## fixtures
* [An environment used to consistently perform tests](https://en.wikipedia.org/wiki/Test_fixture#Software)
* Shared code to setup tests 
* Commonly used in setup, teardown, initializing test objects

## mocking / patching
* To replace components with defined behaviors
* Reduce test dependencies
* https://docs.python.org/3/library/unittest.mock.html

## Measuring how good are tests
* Happy path vs exception handling
* coverage module https://coverage.readthedocs.io/en/7.2.2/
  * `pip install coverage`
* `coverage run --source=calculator unittest_calculator.py && coverage report -m`
* `coverage run --source=calculator test_calculator.py && coverage report -m`

# using the debugger in replit
* Add breakpoints
* Add code in `main.py`

# References
* https://docs.python.org/3/library/unittest.html
* https://docs.pytest.org/en/7.2.x/
* https://docs.python.org/3/library/unittest.mock.html
* https://coverage.readthedocs.io/en/7.2.2/
* https://www.freecodecamp.org/news/how-to-write-unit-tests-for-python-functions/