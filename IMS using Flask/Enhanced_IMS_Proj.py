# Inventory Management System with SQLite, Authentication, and Web UI

## Directory Structure:
# - app.py (Main application file - Flask-based Web App)
# - database.py (Handles SQLite database operations)
# - auth.py (Admin authentication management)
# - inventory.py (CRUD operations for inventory)
# - static/ (CSS, JS files)
# - templates/ (HTML templates for Flask web app)
# - sales.py (Handles sales processing and reports)
# - deleted_products.json (Stores deleted products for recovery)

# Step 1: Setup SQLite Database

import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

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

# Step 2: Fetch Product List

def get_products():
    conn = sqlite3.connect('inventory.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    return products

@app.route('/')
def home():
    return render_template('index.html', products=get_products())

# Step 3: Add New Product

@app.route('/add_product', methods=['POST'])
def add_product():
    conn = sqlite3.connect('inventory.db', check_same_thread=False)
    c = conn.cursor()
    
    prod_id = request.form['id']
    name = request.form['name']
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])
    expiry_date = request.form['expiry_date']
    rating = request.form['rating']
    warranty = request.form['warranty']
    
    c.execute("INSERT INTO products VALUES (?, ?, ?, ?, ?, ?, ?)",
              (prod_id, name, quantity, price, expiry_date, rating, warranty))
    conn.commit()
    conn.close()
    return redirect('/')

# Step 4: Delete Product

@app.route('/delete_product/<prod_id>', methods=['GET'])
def delete_product(prod_id):
    conn = sqlite3.connect('inventory.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("DELETE FROM products WHERE id = ?", (prod_id,))
    conn.commit()
    conn.close()
    return redirect('/')

# Step 5: Purchase Product

@app.route('/purchase', methods=['POST'])
def purchase():
    conn = sqlite3.connect('inventory.db', check_same_thread=False)
    c = conn.cursor()
    
    prod_id = request.form['product_id']
    quantity = int(request.form['quantity'])
    c.execute("SELECT * FROM products WHERE id = ?", (prod_id,))
    product = c.fetchone()
    
    if not product:
        return "Product not found!"
    
    if quantity > product[2]:
        return "Insufficient stock!"
    
    total_price = quantity * product[3]
    name = request.form['customer_name']
    phone = request.form['customer_phone']
    
    c.execute("UPDATE products SET quantity = quantity - ? WHERE id = ?", (quantity, prod_id))
    c.execute("INSERT INTO sales (product_id, quantity, total_price, customer_name, customer_phone) VALUES (?, ?, ?, ?, ?)", 
              (prod_id, quantity, total_price, name, phone))
    conn.commit()
    conn.close()
    
    return redirect('/')

# Step 6: Generate Sales Report

@app.route('/sales_report')
def generate_sales_report():
    conn = sqlite3.connect('inventory.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT * FROM sales")
    sales = c.fetchall()
    conn.close()
    return render_template('sales_report.html', sales=sales)

if __name__ == '__main__':
    init_db()
    app.run(debug=False)

# Step 7: HTML UI (templates/index.html)
# Create the `index.html` file with product listings, add product form, and purchase functionality.