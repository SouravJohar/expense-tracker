import sqlite3
from datetime import datetime

def init():
    '''
    Initialize a new database to store the
    expenditures
    '''
    conn = sqlite3.connect('spent.db')
    c = conn.cursor()
    sql = '''
    CREATE TABLE IF NOT EXISTS expenses (
        amount INTEGER,
        category TEXT,
        message TEXT,
        date TEXT
        )
    '''
    c.execute(sql)
    conn.commit()
    conn.close()

def log(amount, category, message=''):
    '''
    logs the expenditure in the database.
    amount: number
    category: string
    message: (optional) string
    '''
    date = str(datetime.now())
    data = (amount, category, message, date)
    conn = sqlite3.connect('spent.db')
    c = conn.cursor()
    sql = 'INSERT INTO expenses VALUES (?, ?, ?, ?)'
    c.execute(sql, data)
    conn.commit()
    conn.close()

def view(category=None):
    '''
    Returns a list of all expenditure incurred, and the total expense.
    If a category is specified, it only returns info from that
    category
    '''
    conn = sqlite3.connect('spent.db')
    c = conn.cursor()
    if category:
        sql = '''
        SELECT * FROM expenses WHERE category = '{}'
        '''.format(category)
        sql2 = '''
        SELECT sum(amount) FROM expenses WHERE category = '{}'
        '''.format(category)
    else:
        sql = '''
        SELECT * FROM expenses
        '''
        sql2 = '''
        SELECT sum(amount) FROM expenses
        '''
    c.execute(sql)
    results = c.fetchall()
    c.execute(sql2)
    total_amount = c.fetchone()[0]
    conn.close()

    return total_amount, results
