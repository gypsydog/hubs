EMAIL = 'nplotnikov042@gmail.com'
PASSWORD = 'JUA.V77emsm.9NW'

DEFAULT_HEADERS = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
}

SUPPORTED_FORMATS = ('SLDPRT', '3DM', 'IGS', 'STP', 'IGES', 'STEP', 'X_T', 'SAT', 'DXF')
UNSUPPORTED_FORMATS = ('TXT', 'JSON')

HUBS_HOST = 'https://www.hubs.com'
API_URL = '/api/s/cnc'
SIGN_IN_URL = f'{API_URL}/sign-in'
LOGOUT = f'{API_URL}/logout'
JWT_URL = f'{API_URL}/jwt'
UPLOAD_URL = '/api/mr/upload/'

SIGN_IN_DATA = {'email': EMAIL,
                'password': PASSWORD}
