from google.cloud import bigquery
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './client_credentials.json'

client = bigquery.Client()
table_id = "babyname.names_2020"

rows_to_insert = [
    {"name": "makoto", "gender": "M", "count": 2},
    {"name": "tetsu", "gender": "M", "count": 2},
    {"name": "mayuko", "gender": "M", "count": 2},
    {"name": "matsunaga", "gender": "M", "count": 2},
    {"name": "mario", "gender": "M", "count": 2},
]

errors = client.insert_rows_json(table_id, rows_to_insert)
if errors == []:
    print("New rows have been added.")
else:
    print("ERROR")