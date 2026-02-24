import sqlite3
import pandas as pd

conn = sqlite3.connect('web.db')

df = pd.read_csv('analysis-pandas-sql/data/bd_data.csv', index_col=0)
df.index.name = 'index_name'

df.to_sql('data', conn, index_label='index_name', if_exists='replace')

# CREATE TABLE

c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT,
        price DECIMAL(10,2)
        
    ) ''')

# INSERT

c.execute('''
    INSERT OR REPLACE INTO products (
        product_id,
        product_name,
        price)
        
        VALUES (1, 'Computer', 840),
        (2, 'Printer', 1500),
        (3, 'Tablet', 900)       
        
        ''')

# SELECT
c.execute('SELECT * FROM products')
c.fetchone()

# UPDATE
c.execute('UPDATE products SET price=840.50 WHERE product_id = 1')

# DELETE
c.execute('DELETE FROM products WHERE product_id = 3')

conn.commit()
conn.close()



