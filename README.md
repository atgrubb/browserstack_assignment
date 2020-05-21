# AutomateCraigslist
A selenium test suite written in python, connected to jenkins and parallelized in BrowserStack. 

## Requirements

- [x] Write a Selenium test suite using any language/framework and trigger it from a Jenkins server.
- [x] BrowserStack (you will need to create a  [free trial](https://www.browserstack.com/users/sign_up) )
- [x] Contain 3 separate assertions: [Assertion 1](https://github.com/atgrubb/browserstack_assignment/blob/b4da1230cd6fba87af65de79324d7e533b8ab9a3/tests/test_area_page.py#L24), [Assertion 2](https://github.com/atgrubb/browserstack_assignment/blob/b4da1230cd6fba87af65de79324d7e533b8ab9a3/tests/test_area_page.py#L29), [Assertion 3](https://github.com/atgrubb/browserstack_assignment/blob/b4da1230cd6fba87af65de79324d7e533b8ab9a3/tests/test_area_page.py#L38)

*There are a few more assertions and tests in order to better demonstrate parallelization. The sleeps are also there for visualization purposes so you can more easily see how parallelization reduces the execution time of the test suite.*
        
- [x] Run across 5 browsers in parallel

## CI/CD Tech Stack

* [BrowserStack](https://www.browserstack.com/guide/parallel-testing-with-selenium) for executing tests on teh web in parallel across many browsers.
* [jenkins](https://www.jenkins.io/) that is running inside of docker.
* [docker](https://www.docker.com/) for setting up the environment on jenkins for easy execution agnostic of system. This project is technically running a docker container for testing (python-chromedriver) inside a docker container running Jenkins.
* [docker image](https://hub.docker.com/r/joyzoursky/python-chromedriver) for selenium, python and chrome driver.
* [github project](https://github.com/atgrubb/browserstack_assignment)
* [webhook relay](https://webhookrelay.com/blog/2019/04/17/automated-github-pull-request-builds-on-jenkins/) to expose our localhost jenkins publicly in order for the github webhook to be successful. **Important** need to expose port 8080, since that is the default port my jenkins is using.

## Testing Tech Stack

* [selenium for python](https://pypi.org/project/selenium/)
* [pytest](https://docs.pytest.org/en/latest/) for easy execution of the suite from the command line.
* [pytest-xdist](https://www.tutorialspoint.com/pytest/pytest_run_tests_in_parallel.htm) for executing tests in parallel.
* [pycharm](https://www.jetbrains.com/pycharm/) development environment.

## Architecture of Test Suite

The test suite I have written conforms to a page object model for developing tests, with some of my own flare. I'm new to selenium and python but I have written similar models for mobile application testing over the years. I tried to bring some of those learnings over into this project with (hopefully) some success.

The project structure is broken up simply into [pages](https://github.com/atgrubb/browserstack_assignment/tree/master/pages) and [tests](https://github.com/atgrubb/browserstack_assignment/tree/master/tests).

First, the page object.

## [Pages](https://github.com/atgrubb/browserstack_assignment/tree/master/pages)

A page consists of a class that houses all functionality found on a craigslist webpage. In this assignment, full functionality was not implemented in order to keep things simple and easy to grok. A page can in this assignment can be broken down into two (or three) main components - Locators, Actions and Verifications.

#### Locators

Nested classes as a data structure to put all the locators (queries) for elements on that page. These classes aggregate element locators that are related to one another, e.g. locators for the [links under the Jobs header on a craigslist area webpage](https://sfbay.craigslist.org/).

In this project locators are tuples of the form: **(By.Kind, value)**. That is, the method for finding the element (XPATH, CSS Selector, ID, etc.) and the value of the selector.

#### Actions

Actions for clicking, sending keys, etc. on the web page. In this example there are for example actions to clicking Jobs and Housing links. Actions that transition the page return an instance of the webpage that has been navigated to.

In this project, actions accept the aforementioned locators are passed as parameters/arguments in order to perform an action on that element. This greatly reduces the amount of boilerplate code that needs to be written for a page object. The page need only implement a single function for clicking _ALL_ the elements of a locator class. The same is true for verification functions or any other type of function that implements actions that are shared across elements in the same locator class. I really like this pattern.

#### Verifications

Verifications are, like you'd expect, for performing some verification that something happened on that page. These should return True or False. The assertion should therefore be performed in the test case itself.

## [Tests](https://github.com/atgrubb/browserstack_assignment/tree/master/tests)

#### Test Case

A test case should be simple, succint and easy to read. The page object model developed in the assignment leads to a clean and concise test method. Let's just look at an example from the project and see:

```python
def test_click_jobs_header(self):
        search_page = self.area_page.click_jobs_locator(AreaPage.JobsLocators.JOBS_HEADER)
        result = search_page.verify_category_option_selected(SearchPage.CategoriesOptionsLocators.JOBS)
        assert result is True
```

Hopefully it is easy to see: this test clicks the jobs header by supplying the `JOBS_HEADER` locator from `AreaPage` to the `AreaPage` function `click_jobs_locator()`. Since clicking the link will return an instance of `SearchPage`, we set the result of `click_jobs_locator()` to a variable. Then we use `search_page` to verify that we have arrived on the `SearchPage` with the correct category selected, in this case `Jobs`. And that's it - a three line, easy to understand test!

#### Configuration

The [test configuration file](https://github.com/atgrubb/browserstack_assignment/blob/master/tests/conftest.py) utilizes pytest and annotations to do lots of helpful and important stuff for us. Here are some of the notable things this config file does:

* [Parse command line arguments](https://github.com/atgrubb/browserstack_assignment/blob/762205a537ef7eba925d66568680e7db6e207a46/tests/conftest.py#L67) when invoking `py.test`. In this project I'm parsing arguments that then we pass to `BrowserStack` as [desired_capabilities](https://github.com/atgrubb/browserstack_assignment/blob/762205a537ef7eba925d66568680e7db6e207a46/tests/conftest.py#L42).
* Do one-time set up and yield the webdriver so we can set and then reuse the same webdriver instance from test to test.
* Determine if the test is intended to run on `BrowserStack` or not and then have the execution flow proceed accordingly. In this project this is also done via parsing of command line arguments to `py.test`, specifically using the `--browser-stack-enabled True` option.
