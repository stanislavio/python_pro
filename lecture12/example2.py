from typing import Dict

import psycopg2
import psycopg2.extras

dbname = "python_pro"
user = "stas-home"
password = "1qaz1qaz"
host = "localhost"
port = "5432"


def get_connection():
    return psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port,
        cursor_factory=psycopg2.extras.DictCursor
    )


def search_by_name(name: str) -> Dict:
    with get_connection() as connection:
        with connection.cursor() as cursor:
            query = """
                select
                    CONCAT(u.name, ' ', u.surname) as Fullname
                from "user" u
                join address a on u.address_id = a.id
                join city c on a.city_id = c.id
                join country c2 on c.country_id = c2.id
                where u.name ilike Concat('%%', %s, '%%') and phone = %s
                limit 100
            """

            cursor.execute(query, (name,  '32435'))
            result = cursor.fetchall()
            return result


print(search_by_name('sta'))
