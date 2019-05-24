from google.cloud import bigquery

client = bigquery.Client()

user_name = 'Chester Testerson'

sql = '''
SELECT u.FullName, g.*
  FROM Geotag.Geotag g
  JOIN User.User u on u.UserId = g.UserId
 WHERE 1=1
   AND u.FullName = '{user_name}'
'''.format(user_name=user_name)

query_job = client.query(sql)

results = query_job.result()

for row in results:
    print(str(row))

print('Done')
