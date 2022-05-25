# coding=utf-8
from utils.DBUtil import sqlite


@sqlite
def get_nav(cur):
    cur.execute('select * from blog_nav ')
    rows = cur.fetchall()
    for row in rows:
        print(row)




if __name__ == '__main__':
    get_nav()