import psycopg2
from config import config


def update_vendor(vendor_name, vendor_id):
    sql = 'Update vendors set vendor_name = %s where vendor_id = %s'
    conn = None
    update_rows = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (vendor_name, vendor_id))
        update_rows = cur.rowcount
        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return update_rows


if __name__ == '__main__':
    update_vendor("3M Corp", 1)