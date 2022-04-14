import copy
import json
from os import walk
from requests_toolbelt import MultipartEncoder
from checkers import check_response_code, check_ok
from client import Client
from const import DEFAULT_HEADERS, HUBS_HOST
from logger import step

hubs = Client(HUBS_HOST)


@step('Get token')
def get_token() -> str:
    token_response = hubs.jwt()
    check_ok(token_response)
    jwt_token = json.loads(token_response.text)['jwt']
    return jwt_token


@step('Update headers with authorization token')
def update_headers_token():
    token = get_token()
    DEFAULT_HEADERS.update({'authorization': f'Bearer {token}'})


@step('Prepare test models for usage in test parametrization')
def get_models_paths(formats):
    _, _, filenames = next(walk('test_models'), (None, None, []))
    paths = {}
    for name in filenames:
        for format in formats:
            if format in name:
                paths[name.split('.')[1]] = f'test_models/{name}'
    return paths


def upload_model(file_path: str,
                 tech: str = 'cnc-machining',
                 unit: str = 'mm',
                 extrusion_height: str = '1',
                 expected_code: int = 202,):
    file_name = file_path.split('/')[1]

    with open(file_path, 'rb') as file:
        payload = MultipartEncoder(
            fields={
                'technology': tech,
                'unit': unit,
                'extrusion_height': extrusion_height,
                'file': (file_name, file, 'text/plain')
            }
        )
        headers = copy.deepcopy(DEFAULT_HEADERS)
        headers.update({'Content-Type': payload.content_type})
        upload_response = hubs.upload(payload, headers)

    check_response_code(upload_response, expected_code=expected_code)
