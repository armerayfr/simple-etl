import csv
import sqlalchemy
from sqlalchemy import create_engine, text


def sales_month_report():
    engine = create_engine('sqlite:///data.db')

    conn = engine.connect()

    query = text("""
        SELECT 
            strftime('%m', tgl_transaksi) as month,
            SUM(pembayaran) as total
        FROM transaksi
            GROUP BY month;
    """)

    res = conn.execute(query)

    with open('sales_month.csv', 'w', newline="") as csv_file:
        writer = csv.writer(csv_file)

        for dt in res:
            writer.writerow(dt)

    conn.close()

def sales_product_report():
    engine = create_engine('sqlite:///data.db')

    conn = engine.connect()

    query = text("""
        SELECT 
            id_produk,
            SUM(pembayaran)
        FROM transaksi
            GROUP BY id_produk;
    """)

    res = conn.execute(query)

    with open('sales_product.csv', 'w', newline="") as csv_file:
        writer = csv.writer(csv_file)

        for dt in res:
            writer.writerow(dt)

    conn.close()

