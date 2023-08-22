import psycopg2
import psycopg2.extras

dbname = "python_pro"
user = "stas-home"
password = "1qaz1qaz"
host = "localhost"
port = "5432"


connection = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port,
    cursor_factory=psycopg2.extras.DictCursor
)

cursor = connection.cursor()
query = """
SELECT name as hello FROM "user";
"""
cursor.execute(query)

# cursor.fetchall()
# cursor.fetchone()
# cursor.fetchmany(size=5)

users = cursor.fetchall()
for user in users:
    print(user['hello'])

# Закриття курсору
cursor.close()

# Застосування змін та закриття з'єднання
connection.commit()
connection.close()
