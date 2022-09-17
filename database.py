import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    database = 'crypto_rates',
    user = 'postgres',
    password = 'postgres',
    port = '5432'
)

cursor = conn.cursor()

# cursor.execute("""SELECT * FROM rates""")
# rows = cursor.fetchall()
# print(rows)

#cursor.execute("""SELECT * FROM rates""" )

database_delete = """DELETE FROM rates"""
cursor.execute(database_delete)


# This commits the transaction. Commit the changes.
conn.commit()

# Closes the cursor
cursor.close()

# Closes the connection to the database.
conn.close()

