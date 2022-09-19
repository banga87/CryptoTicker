# from locale import currency
import psycopg2

conn = psycopg2.connect(
    host = 'ec2-35-170-146-54.compute-1.amazonaws.com',
    database = 'dd549hlvu4r6d',
    user = 'gzbsduawjbecah',
    password = '441d31fb8bd2356e7cc62255b242ecf12047de22b164625673f3e269fddaa6b5',
    port = '5432'
)
cursor = conn.cursor()

cursor.execute("""ALTER TABLE rates ADD PRIMARY KEY (ticker)""")

conn.commit()
cursor.close()
conn.close()