import allure
import pytest
from _pytest.fixtures import fixture
from checkers import check_ok
from client import Client
from const import HUBS_HOST, SUPPORTED_FORMATS, UNSUPPORTED_FORMATS
from helpers import update_headers_token, get_models_paths, upload_model

hubs = Client(HUBS_HOST)


@fixture(scope='session')
def login_headers():
    with allure.step('Get anonymous token'):
        anonymous_headers = update_headers_token()
    with allure.step('Login'):
        sign_in_response = hubs.sign_in(headers=anonymous_headers)
        check_ok(sign_in_response)
    with allure.step('Get user token'):
        headers = update_headers_token()
    yield headers
    hubs.logout()


@pytest.mark.parametrize('tech', ['cnc-machining', 'sheet-metal'])
@pytest.mark.parametrize('file_path',
                         get_models_paths(SUPPORTED_FORMATS).values(),
                         ids=get_models_paths(SUPPORTED_FORMATS).keys())
def test_model_upload(file_path, tech, login_headers):
    upload_model(headers=login_headers,
                 file_path=file_path,
                 tech=tech,
                 expected_code=202)


@pytest.mark.parametrize('tech', ['cnc-machining', 'sheet-metal'])
@pytest.mark.parametrize('file_path',
                         get_models_paths(UNSUPPORTED_FORMATS).values(),
                         ids=get_models_paths(UNSUPPORTED_FORMATS).keys())
def test_model_upload_negative(file_path, tech, login_headers):
    upload_model(headers=login_headers,
                 file_path=file_path,
                 tech=tech,
                 expected_code=400)
