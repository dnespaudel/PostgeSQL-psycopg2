import psycopg2
from config import config


def add_part(part_name, vendor_name):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('Call add_new_part(%s,%s)', (part_name, vendor_name))
        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    add_part('OLED', 'LG')