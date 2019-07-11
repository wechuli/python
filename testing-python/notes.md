# Tests

## Why Test

- Reduce bugs in existing code
- Ensure bugs that are fixed stay fixed
- Ensure that new features don't break old ones
- Ensure that cleaning up code doesn't introduce new bugs

## Test Driven Development

- Development begins by written tests
- Once tests are written, write code to make tests pass
- Once tests pass, a feature is considered complete

### Red, Green, Refactor

1. Red - Write a test that fails
2. Green - Write the minimal amount of code necessary to make the test pass
3. Refactor - Clean up the code, while ensuring that tests still pass

### Assertions

- We can make simple assertions with the `assert` keyword
- `assert` accepts an expression
- Return `None` if the expression is truthy
- Raises an AssertionError if the expression is falsy
- Accepts an optional error message as a second argument

`assert` is not a function, it is a statement. If a Python file is run with the -O flag, assertions will be ignored

### Dottests

We can write tests for functions inside of the docstring
Write code that looks like it's inside of a REPL
To run a file with doctests

        python -m doctest -v {file_name}.py

#### Issues with doctests

- Unfamiliar syntax
- Clutters up our function code
- Lacks many features or larger testing tools
- Tests can be brittle

## Unit Testing
- Test smallest part of an application in isolation(e.g. units)
- Good candidates for unit testing: individual classes, modules or functions
- Bad candidates for unit testing: an entire application, dependencies across several classes or modules

### unittest framework
In built module for testing 
You can write unit tests encapsulated as classes that inherit from `unittest.TestCase`
This inheritence gives you access to may assertion helpers that let you test the behaviour of your functions.
You can run tests by calling `unittest.main()`

To run tests with more information, add docstrings to your testing methods and use the `-v` flag when executing the test file.

#### Other Types of Assertions
- `self.assertEqual(x,y)`
- `self.assertNotEqual(x,y)`
- `self.assertTrue(x)`
- `self.assertFalse(x)`
- `self.assertIsNone(x)`
- `self.assertIsNotNone(x)`
- `self.assertIn(x,y)`
- `self.assertNotIn(x,y)`
- ..more


