import sqlalchemy
from sqlalchemy import create_engine, text


def create_table():
    engine = create_engine('sqlite:///data.db')

    conn = engine.connect()

    conn.execute(text("""CREATE TABLE IF NOT EXISTS transaksi(
        id_transaksi VARCHAR PRIMARY KEY,
        tgl_transaksi DATE,
        id_pembeli VARCHAR,
        id_produk VARCHAR,
        pembayaran INTEGER,
        data_source VARCHAR,
        timestamp datetime DEFAULT CURRENT_TIMESTAMP)"""))