import dotmap

database = dotmap.DotMap({
    "url": "192.168.0.14",
    "port": 3306,
    "user": "root",
    "password": "ddc.2017",
    "database_name": "oa_manpower"
})

dbpath = "../db.sqlite3"
