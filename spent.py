import sqlite3 as db


def init():
    '''
    Initialize a new database to store the
    expenditures
    '''
    conn = db.connect("spent.db")
    cur = conn.cursor()
    sql = '''
    create table if not exists expenses (
        amount number,
        category string,
        message string,
        date string
        )
    '''
    cur.execute(sql)
    conn.commit()


def log(amount, category, message=""):
    '''
    logs the expenditure in the database.
    amount: number
    category: string
    message: (optional) string
    '''
    from datetime import datetime
    date = str(datetime.now())
    conn = db.connect("spent.db")
    cur = conn.cursor()
    sql = '''
    insert into expenses values (
         {},
        '{}',
        '{}',
        '{}'
        )
    '''.format(amount, category, message, date)
    cur.execute(sql)
    conn.commit()


def view(category=None):
    '''
    Returns a list of all expenditure incurred, and the total expense.
    If a category is specified, it only returns info from that
    category
    '''
    conn = db.connect("spent.db")
    cur = conn.cursor()
    if category:
        sql = '''
        select * from expenses where category = '{}'
        '''.format(category)
        sql2 = '''
        select sum(amount) from expenses where category = '{}'
        '''.format(category)
    else:
        sql = '''
        select * from expenses
        '''.format(category)
        sql2 = '''
        select sum(amount) from expenses
        '''.format(category)
    cur.execute(sql)
    results = cur.fetchall()
    cur.execute(sql2)
    total_amount = cur.fetchone()[0]

    return total_amount, results
