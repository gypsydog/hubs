import allure
import requests
from hamcrest import assert_that, any_of
from requests import codes

from logger import step


@step('Check that response has expected status code')
def check_response_code(response: requests.Response, expected_code: int = codes.ok) -> None:
    if response.status_code == 429:
        message = 'ERROR: Too many sign in attempts.Please try again later.'
    else:
        message = (
            f'Expected status code: {expected_code}. Actual code: {response.status_code}.'
        )
    allure.attach(message)

    assert_that(response.status_code, any_of(expected_code), message)


@step('Check code 200')
def check_ok(response: requests.Response) -> None:
    check_response_code(response, expected_code=codes.ok)
