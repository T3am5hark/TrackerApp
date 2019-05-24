import json
from flask import Flask, request, abort

from google.cloud import bigquery
from src.util.log_utils import init_logging

app = Flask(__name__)
logger = init_logging()


@app.route("/api/v1/RetrieveForUser", methods=['GET'])
def get_for_user():

    log_inbound(request)
    user_id = request.args.get('userId', None)

    sql = '''
        SELECT u.FullName, g.*
          FROM Geotag.Geotag g
          JOIN User.User u on u.UserId = g.UserId
        WHERE 1=1
        AND u.UserId = {user_id}
    '''.format(user_id=user_id)



@app.route("/api/v1/PostTag", methods=['POST'])
def post_geotag():

    log_inbound(request)

    user_id = request.form.get('userId', None)
    latitude = request.form.get('latitude', None)
    longitude = request.form.get('longitude', None)
    application = request.form.get('application', '')

    sql = '''
        INSERT INTO Geotag.Geotag
        (UserId, CreatedTimestamp,
        Geotag, Application)
        VALUES
        ('{user_id}', CURRENT_TIMESTAMP(),
         ST_GEOGPOINT({long}, {lat}), '{app}')
        '''.format(user_id=user_id,
                   lat=latitude,
                   long=longitude,
                   app=application)

    logger.debug(sql)

    try:
        client = bigquery.Client()
        query_job = client.query(sql)
        results = query_job.result()
        response = {'success': 1, 'error': None}
    except Exception as ex:
        response = {'success': 0, 'error': str(ex)}

    return json.dumps(response)


def log_inbound(req):
    logger.info('Received inbound request from {0}'.format(req.remote_addr))
    logger.debug(request.json)


if __name__ == "__main__":

    logger.info('Starting Flask service...')
    app.run(host='0.0.0.0')

