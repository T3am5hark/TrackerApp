from google.cloud import bigquery
from time import sleep

client = bigquery.Client()

user_id = '17be08c2-c50f-4446-8815-ae2679964f0f'

sql = '''
INSERT INTO Geotag.Geotag
(UserId, CreatedTimestamp,
 Geotag, Application)
VALUES
('{user_id}', CURRENT_TIMESTAMP(),
 ST_GEOGPOINT(40.7484, -73.9857), 'test')
'''.format(user_id=user_id)

print(sql)

n = 50

for i in range(1,n+1):
    print('Inserting {} of {}'.format(i, n))

    query_job = client.query(sql)

    results = query_job.result()

    sleep(0.25)


print('Done')
