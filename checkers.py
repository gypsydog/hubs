import allure
import requests
from hamcrest import assert_that, equal_to
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

    assert_that(response.status_code, equal_to(expected_code), message)


@step('Check that response has expected text')
def check_response_text(response: requests.Response, expected_text: str):
    message = (
        f'Expected response.text: {expected_text}. Actual text: {response.text}.'
    )
    allure.attach(message)

    assert_that(response.text, equal_to(expected_text), message)


@step('Check code 200')
def check_ok(response: requests.Response) -> None:
    check_response_code(response=response,
                        expected_code=codes.ok)


@step('Check upload unsupported file type')
def check_unsupported_file_type_text(response: requests.Response):
    expected_text = '{"file":["Unsupported file type"]}\n'
    check_response_text(response=response,
                        expected_text=expected_text)
