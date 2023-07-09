import os
import psycopg2
db = psycopg2.connect(os.environ.get('DATABASE_URL'))
