import sqlite3
from flask import redirect

def add_product(request):
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

def delete_product(prod_id):
    conn = sqlite3.connect('inventory.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("DELETE FROM products WHERE id = ?", (prod_id,))
    conn.commit()
    conn.close()
    return redirect('/')