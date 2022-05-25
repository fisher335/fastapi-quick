import sqlite3 as sl

con = sl.connect('./db.sqlite3')


def get_all(table):
    sql = 'select * from %s' % table
    con.execute(sql)
    value = con.fetchall()
    return value


def get_all_user():
    with con:
        cur = con.cursor()
        cur.execute('select * from blog_nav ')
        value = cur.fetchall()
        return value


if __name__ == '__main__':
    print(get_all_user())
