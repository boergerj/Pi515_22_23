# Unit Testing in Python

* What is unit-testing?
* Why do unit-testing?
* When to run unit-tests?
* What unit-test is not?


# Let's write some unit tests

## Quick tour of `Calculator`
* Integer calculations only
* What happens when we enter floats?
* Execute [`calculator.py`](calculator.py)

## Built-in `unittest` module (PyUnit)
* https://docs.python.org/3/library/unittest.html
* No extra dependencies.
* Standard convention.
* Rather verbose.
* Example: [`unittest_calculator.py`](unittest_calculator.py)

```
> python unittest_calculator.py
```

## `pytest` package (PyTest)
* https://docs.pytest.org/en/7.2.x/
  * `pip install pytest`
* Great plugin supports.
* Simpler syntax.
* Example: [`test_calculator.py`](test_calculator.py)

```
> python test_calculator.py
```

## fixtures
* [An environment used to consistently perform tests](https://en.wikipedia.org/wiki/Test_fixture#Software)
* Shared code to setup tests 
* Commonly used in setup, teardown, initializing test objects

### exercise
* Add more tests?

## mocking / patching
* To replace components with defined behaviors
* Reduce test dependencies
* https://docs.python.org/3/library/unittest.mock.html
* Example: [`mock_demo.py`](mock_demo.py)

## Measuring how good are tests
* Happy path vs exception handling
* coverage module https://coverage.readthedocs.io/en/7.2.2/
  * `pip install coverage`
* `coverage run --source=calculator unittest_calculator.py && coverage report -m`
* `coverage run --source=calculator test_calculator.py && coverage report -m`

## exercise
* Cheese out coverage?

# using the debugger in replit
* Add breakpoints
* Add code in `main.py` and run it

## exercise
* reader internal values
* recursion stacks

# Take aways
* Unit-testing is part of the development process we commonly do (formally or not).
* `PyUnit` or `PyTest` are easy to integrate with existing codebase or new projects.
* Focusing on unit under test with fixtures or mocks to simplify setups.
* Debugger can simplify troubleshooting greatly than adding print statements.

# References
* https://docs.python.org/3/library/unittest.html
* https://docs.pytest.org/en/7.2.x/
* https://docs.python.org/3/library/unittest.mock.html
* https://coverage.readthedocs.io/en/7.2.2/
* https://www.freecodecamp.org/news/how-to-write-unit-tests-for-python-functions/