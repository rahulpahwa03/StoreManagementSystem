import sqlite3

sql_create = """
CREATE TABLE IF NOT EXISTS orders(
id INTEGER PRIMARY KEY,
item text,
customer text,
seller text,
price text
);
"""

# fetching all the values from the database
sql_fetch = 'SELECT * FROM orders'

# adding order to database
add_order = 'INSERT INTO orders VALUES(null, ?, ?, ?, ?)'

# removing from database
remove_order = 'DELETE FROM orders WHERE id=?'

# updating
update_order = 'UPDATE orders SET item =?, customer = ?, seller = ?, price = ? WHERE id = ?'


# class for database

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(sql_create)
        self.conn.commit()

    def fetch(self):
        self.cur.execute(sql_fetch)
        return self.cur.fetchall()

    def insert(self, item, customer, seller, price):
        self.cur.execute(add_order, (item, customer, seller, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute(remove_order, (id, ))
        self.conn.commit()

    def update(self, id, item, customer, seller, price):
        self.cur.execute(update_order, (id, item, customer, seller, price))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


db = Database('store.db')

