from flask import Flask, render_template, request, redirect
from database import init_db, get_products
from inventory import add_product, delete_product
from sales import purchase_product, generate_sales_report

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', products=get_products())

# Route to display the Add Product form
@app.route('/add_product', methods=['GET'])
def add_product_page():
    return render_template('add_product.html')

# Route to handle adding a new product
@app.route('/add_product', methods=['POST'])
def add_product_route():
    return add_product(request) 

# Route to display the Purchase Product form
@app.route('/purchase_product', methods=['GET'])
def purchase_product_page():
    return render_template('purchase_product.html')

# Route to handle purchasing a product
@app.route('/purchase_product', methods=['POST'])
def purchase_product_route():
    return purchase_product(request)

# Route to delete a product
@app.route('/delete_product/<prod_id>', methods=['POST'])
def delete_product_route(prod_id):
    return delete_product(prod_id)

# Route to view sales report
@app.route('/sales_report')
def sales_report_route():
    return generate_sales_report()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)