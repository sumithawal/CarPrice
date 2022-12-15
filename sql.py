import sqlite3
import os

if os.path.exists('reviews.sqlite'):
    os.remove('reviews.sqlite')

conn = sqlite3.connect('reviews.sqlite')
c = conn.cursor()

c.execute('CREATE TABLE review_db'
          ' (Year INTEGER, Present_Price INTEGER, Kms_Driven INTEGER, Owner INTEGER, Fuel_Type_sql TEXT,Seller_Type_sql TEXT, Transmission_sql TEXT, predicted_price FLOAT)')

conn.commit()
conn.close()
