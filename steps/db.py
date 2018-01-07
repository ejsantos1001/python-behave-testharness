import MySQLdb


def query(x):
    db = MySQLdb.connect("localhost","root","pass","employees")
    cursor = db.cursor()
    cursor.execute(x)
    data = cursor.fetchone()
    db.close()
    return data






