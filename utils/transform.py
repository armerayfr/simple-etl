def fill_null(dt):
    if dt:
        for rec in dt:
            if not rec['potongan_harga'] or rec['potongan_harga'] == 'None':
                rec['potongan_harga'] = 0

            # convert str potongan_harga into int
            if isinstance(rec['potongan_harga'], str):
                rec['potongan_harga'] = int(rec['potongan_harga'])
    return dt


def make_payment(dt, brand):
    for rec_sale in dt:
        for rec_brand in brand:
            """
                buat pembayaran: harga (brand) - potongan_harga (sale)
            """ 
            if rec_sale['id_produk'] == rec_brand['id_produk']:
                rec_sale['pembayaran'] = rec_brand['harga'] - rec_sale['potongan_harga']
    return dt


def formating_date(dt):
    for rec in dt:
        if not isinstance(rec['tgl_transaksi'], str):
            rec['tgl_transaksi'] = rec['tgl_transaksi'].strftime("%Y-%m-%d")

        rec['tgl_transaksi'] = rec['tgl_transaksi'].replace('/', '-')

    return dt


def sales_transform(data, data_brand):
    # handling missing value
    data = fill_null(data)

    # make payment column
    data = make_payment(data, data_brand)

    # formating date: '2022-01-03'
    data = formating_date(data)
    return data
