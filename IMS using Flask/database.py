import sqlite3

def init_db():
    conn = sqlite3.connect('inventory.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS products (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    quantity INTEGER,
                    price REAL,
                    expiry_date TEXT,
                    rating TEXT,
                    warranty TEXT)
                ''')
    c.execute('''CREATE TABLE IF NOT EXISTS sales (
                    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id TEXT,
                    quantity INTEGER,
                    total_price REAL,
                    customer_name TEXT,
                    customer_phone TEXT,
                    sale_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
                ''')
    conn.commit()
    conn.close()

def get_products():
    conn = sqlite3.connect('inventory.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    return products