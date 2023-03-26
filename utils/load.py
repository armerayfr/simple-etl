import sqlalchemy
from sqlalchemy import create_engine, text


def insert_to_sql(list_data, source):
    engine = create_engine('sqlite:///data.db')

    conn = engine.connect()

    list_data = [dict(rec, data_source=source)for rec in list_data]
    print(list_data)

    insert = text("""
        INSERT INTO
            transaksi(
                id_transaksi,
                tgl_transaksi,
                id_pembeli,
                id_produk,
                pembayaran,
                data_source
            )
            VALUES(
                :id_transaksi,
                :tgl_transaksi,
                :id_pembeli,
                :id_produk,
                :pembayaran,
                :data_source
            )
    """)

    for rec in list_data:
        conn.execute(insert, rec)

    conn.close()
