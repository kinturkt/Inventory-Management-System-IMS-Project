import sqlite3

# Define a diverse list of sample products (40+ entries, including expiry dates)
sample_products = [
    ("2001", "Smartphone", 50, 699.99, "No Expiry", "4.5", "24 months"),
    ("2002", "Laptop", 30, 1200.50, "No Expiry", "4.7", "36 months"),
    ("2003", "Headphones", 100, 150.00, "No Expiry", "4.3", "12 months"),
    ("2004", "Milk", 200, 2.99, "2025-03-10", "4.8", "N/A"),
    ("2005", "Bread", 150, 1.99, "2025-02-28", "4.5", "N/A"),
    ("2006", "Butter", 80, 4.99, "2025-04-15", "4.7", "N/A"),
    ("2007", "Cheese", 90, 5.99, "2025-05-20", "4.6", "N/A"),
    ("2008", "Eggs", 120, 3.99, "2025-03-05", "4.9", "N/A"),
    ("2009", "Yogurt", 75, 1.49, "2025-03-25", "4.8", "N/A"),
    ("2010", "Medicine A", 50, 12.99, "2026-07-10", "4.4", "N/A"),
    ("2011", "Vitamin C", 60, 14.99, "2026-12-15", "4.7", "N/A"),
    ("2012", "Pain Reliever", 40, 9.99, "2026-09-30", "4.5", "N/A"),
    ("2013", "Shampoo", 100, 8.99, "No Expiry", "4.6", "N/A"),
    ("2014", "Soap", 150, 2.49, "No Expiry", "4.4", "N/A"),
    ("2015", "Toothpaste", 120, 3.99, "No Expiry", "4.7", "N/A"),
    ("2016", "Coffee", 90, 7.99, "2025-12-31", "4.5", "N/A"),
    ("2017", "Tea", 85, 6.49, "2025-11-20", "4.6", "N/A"),
    ("2018", "Canned Beans", 110, 1.99, "2027-05-10", "4.4", "N/A"),
    ("2019", "Rice", 200, 15.99, "2027-08-15", "4.8", "N/A"),
    ("2020", "Washing Machine", 10, 599.99, "No Expiry", "4.5", "48 months"),
    ("2021", "Refrigerator", 15, 999.99, "No Expiry", "4.8", "60 months"),
    ("2022", "Microwave Oven", 30, 199.99, "No Expiry", "4.4", "36 months"),
    ("2023", "Air Conditioner", 12, 1200.00, "No Expiry", "4.6", "48 months"),
    ("2024", "Ceiling Fan", 50, 49.99, "No Expiry", "4.3", "36 months"),
    ("2025", "Water Heater", 20, 250.00, "No Expiry", "4.5", "48 months"),
    ("2026", "Iron", 80, 39.99, "No Expiry", "4.2", "24 months"),
    ("2027", "Juice", 50, 3.99, "2025-04-10", "4.5", "N/A"),
    ("2028", "Frozen Pizza", 40, 6.99, "2025-06-15", "4.6", "N/A"),
    ("2029", "Energy Drink", 60, 2.99, "2025-05-01", "4.4", "N/A"),
    ("2030", "Chocolate Bar", 90, 1.49, "2025-09-30", "4.8", "N/A"),
    ("2031", "Toaster", 50, 49.99, "No Expiry", "4.1", "24 months"),
    ("2032", "Blender", 30, 69.99, "No Expiry", "4.3", "24 months"),
    ("2033", "Electric Kettle", 40, 39.99, "No Expiry", "4.4", "24 months"),
    ("2034", "Hair Dryer", 45, 29.99, "No Expiry", "4.2", "12 months"),
    ("2035", "Smartwatch", 35, 199.99, "No Expiry", "4.7", "24 months"),
    ("2036", "Fitness Tracker", 50, 99.99, "No Expiry", "4.5", "18 months"),
    ("2037", "VR Headset", 25, 399.99, "No Expiry", "4.6", "36 months"),
    ("2038", "Projector", 20, 499.99, "No Expiry", "4.5", "36 months"),
    ("2039", "Gaming Console", 30, 499.99, "No Expiry", "4.8", "48 months"),
    ("2040", "Portable Speaker", 40, 89.99, "No Expiry", "4.5", "24 months"),
]

# Connect to SQLite database
db_path = "inventory.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Create products table
c.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id TEXT PRIMARY KEY,
        name TEXT,
        quantity INTEGER,
        price REAL,
        expiry_date TEXT,
        rating TEXT,
        warranty TEXT
    )
""")

# Insert sample data
c.executemany("INSERT OR IGNORE INTO products VALUES (?, ?, ?, ?, ?, ?, ?)", sample_products)

# Commit and close connection
conn.commit()
conn.close()

# Provide the database file path
db_path = "inventory.db"