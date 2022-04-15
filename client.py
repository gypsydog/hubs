import allure

import requests

from const import (
    DEFAULT_HEADERS,
    SIGN_IN_DATA,
    SIGN_IN_URL,
    JWT_URL,
    UPLOAD_URL,
    LOGOUT,
)
from logger import step


class Client:
    def __init__(self, host: str, headers: dict = None):
        if not host:
            raise AttributeError('Attribute host should not be empty.')
        self.host = host
        self.headers = headers
        self.session = requests.session()

    def _send_request(self, method: str, path: str, **kwargs) -> requests.Response:
        url = f'{self.host}{path}'
        params = (kwargs.get('params', None),)
        data = (kwargs.get('data', None),)
        if method.lower() == 'get':
            payload = params
        else:
            payload = data
        headers = kwargs.pop('headers', self.headers)
        allure.attach(
            f'  REQUEST: {method} {url} \n'
            f'  PAYLOAD: {payload} \n'
            f'  HEADERS: {headers}\n'
        )
        response = self.session.request(method=method,
                                        url=url,
                                        headers=headers,
                                        **kwargs)
        allure.attach(
            f'  RESPONSE: {response.status_code}\n'
            f'  TEXT: {response.text}\n'
            f'  HEADERS: {response.headers}\n'
        )
        return response

    def _post(self, url: str, payload: dict = None, headers: dict = None) -> requests.Response:
        payload = {} if payload is None else payload
        headers = DEFAULT_HEADERS if headers is None else headers
        response = self._send_request('post', path=url, data=payload, headers=headers)
        return response

    def _get(self, url: str, payload: dict = None, headers: dict = None) -> requests.Response:
        payload = {} if payload is None else payload
        headers = DEFAULT_HEADERS if headers is None else headers
        response = self._send_request('get', path=url, params=payload, headers=headers)
        return response

    @step('Sign in')
    def sign_in(self, sign_in_data: dict = SIGN_IN_DATA, headers: dict = DEFAULT_HEADERS) -> requests.Response:
        sign_in_response = self._post(url=SIGN_IN_URL, headers=headers, payload=sign_in_data)
        return sign_in_response

    @step('Send GET jwt request')
    def jwt(self) -> requests.Response:
        token_response = self._get(url=JWT_URL)
        return token_response

    @step('Upload model')
    def upload(self, payload, headers: dict = DEFAULT_HEADERS) -> requests.Response:
        upload_response = self._post(url=UPLOAD_URL, headers=headers, payload=payload)
        return upload_response

    @step('Logout')
    def logout(self) -> requests.Response:
        logout_response = self._get(url=LOGOUT)
        return logout_response
