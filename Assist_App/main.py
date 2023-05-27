import psycopg2 as psy
from funciones_auxiliares import *
from clases import *

conn = psy.connect(dbname = 'asisst',user = 'postgres', password = 'rodriyadri20')
cur = conn.cursor()

app = entrevista()
app.run()
