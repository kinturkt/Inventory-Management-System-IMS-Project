import sqlite3
from flask import render_template, redirect

def purchase_product(request):
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

def generate_sales_report():
    conn = sqlite3.connect('inventory.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT * FROM sales")
    sales = c.fetchall()
    conn.close()
    return render_template('sales_report.html', sales=sales)