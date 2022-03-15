import psycopg2
from config import config


def get_parts(vendor_id):
    """ get parts provided by a vendor specified by the vendor_id"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.callproc('get_parts_by_vendor', (vendor_id,))
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    get_parts(3)