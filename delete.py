import psycopg2
from config import config


def delete_part(part_id):
    """ delete part by part id"""
    conn = None
    rows_deleted = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("Delete from parts where part_id = %s", (part_id,))
        rows_deleted = cur.rowcount
        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted


if __name__ == '__main__':
    deleted_row = delete_part(2)