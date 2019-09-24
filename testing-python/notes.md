# Tests

A unit is a small piece of code generally part of a larger system. It could be -

- a method or a function
- a module or class
- a small group of related classes

An automated Unit test is designed by a human. Runs without intervention and Reports either 'pass' or fail.

It's not a unit test if it uses:

- the Filesystem
- a Database
- the Network

## Test Suite

Test suite is a container that has a set of tests which helps testers in executing and reporting the test execution status.A test case can be added to multiple test suites and test plans. After creating a test plan, test suites are created which in turn can have any number of tests. A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.

### Test Fixture

A software test fixture sets up the system fo the testing process by providing it with all the necessary code to initialize it, thereby satisfying whatever preconditions there may be. An example could be loading up a database with knwon parameters from a customer site before running your test. A test fixture represents the preparation needed to perform one or more tests an any associate cleanup actions. This may involve, for example, creating temporary or proxy databases, directories or starting a server process.

### Test case

A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs. `unittest` provides a base class, `TestCase`, which may be used to create new test cases.

### test runner

A test runner is a component which orchestrates the execution of tests and provides the outcome to the user. The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.

### Three Parts of a Test

- **Arrange** - Set up the object to be tested and colaborators
- **Act** - Exercise the unit under test
- **Assert** - Make claims about what happened

## Why Test

- Reduce bugs in existing code
- Ensure bugs that are fixed stay fixed
- Ensure that new features don't break old ones
- Unit tests help you to understand what to build
- Help to document the units
- Helps in designing the units
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

### Before and After Hooks

- For larger applications, you may want similar application state before running tests
- `setUp` runs before each test method
- `tearDown` runs after each test method
- Common use cases: adding/removing data from a test database, creating instances of a class

### Documenting the Units

- Specify the behavious of the unit under test
- How the original developer intended the unit to be used
- Executable: keeps in sync with the unit inder test

### Unit Test help with better design of the units

- Decompose into testable units. Loose Coupling and High Cohesion
- Design interface interface and implementation separately

### Regression

Ensure previously developed and tested software still performs after a change.

### Limitations of Unit Testing

- Hard to write if units have many dependencies
- Test scenarios may not occur in production, you need to find relevant cases
- Tests may not notice failures
- Unit tests do not find integration or non-functional problems

Unit testing is part of your job. Fit automated test in your development process.

### Tests Support Collaboration

- Pull changes from version control
- Run the tests and check they pass before changing code
- Run the tests again before sharing your changes

### Build Automation Server
- Detects changes from version control, fetches them
- Builds the code and runs the tests
- Communicates the result to developers
- If passing tests- deploys to manual testing environment

Make frequent, small commits and run tests on each one.