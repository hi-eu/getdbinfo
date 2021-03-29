import boto3
import psycopg2

ssm = boto3.client('ssm')
username_parameter = ssm.get_parameter(Name='/rds/db/postgresql/superuser/username', WithDecryption=True)
password_parameter = ssm.get_parameter(Name='/rds/db/postgresql/superuser/password', WithDecryption=True)
host_parameter = ssm.get_parameter(Name='/rds/db/postgresql/host', WithDecryption=True)
endpoint_parameter    = ssm.get_parameter(Name='/rds/db/postgresql/endpoint', WithDecryption=True)
username = username_parameter['Parameter']['Value']
password = password_parameter['Parameter']['Value']
host = host_parameter['Parameter']['Value']
endpoint = endpoint_parameter['Parameter']['Value']
con = psycopg2.connect(database="postgres", user=username, password=password, host=host)
cur = con.cursor()
cur.execute('''SELECT version();''')
row = cur.fetchone()
print("PostgreSQL database Username: ")
print(username)
print('PostgreSQL database Endpoint:')
print(endpoint)
print('PostgreSQL database Version:')
print(row)
con.commit()
con.close()
