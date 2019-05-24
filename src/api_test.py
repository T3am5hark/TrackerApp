import requests
from src.util.log_utils import init_logging

HEADERS = {'User-Agent': 'Mozilla/5.0',
           'Accept': 'application/json'}

# Chester Testerson
user_id = '17be08c2-c50f-4446-8815-ae2679964f0f'
server = 'http://localhost:5000'
service_url = server + '/api/v1/PostTag'
logger = init_logging('api_test')

logger.info('Testing API...')

n = 3
for i in range(1, n+1):
    logger.info('{} of {}'.format(i, n))

    data = {'userId': user_id,
            'latitude': 32.2226,
            'longitude': -110.9747,
            'application': 'api_test.py'}

    try:
        session = requests.Session()
        result = session.post(service_url,
                              data=data,
                              headers=HEADERS,
                              timeout=30)

        result_json = result.json()

        if result_json.get('success', 0) != 1:
            logger.error('Server responded with error:')
            logger.error(result_json.get('error', '<no error messsage>'))
        else:
            logger.info('success')

    except Exception as ex:
        logger.exception(str(ex))




