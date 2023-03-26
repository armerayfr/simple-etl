from utils.extract import sales_csv_to_list, sales_xlsx_to_list, brand_xlsx_to_list
from utils.transform import sales_transform
from utils.data_warehouse import create_table
from utils.load import insert_to_sql
from utils.reporting import sales_month_report, sales_product_report

sales_a = 'sales_A.csv'
sales_b = 'sales_B.xlsx'
brand = 'brand.xlsx'

if __name__ == '__main__':
    # implement data warehouse
    dt_wh = create_table()

    # extract process
    data_sales_a = sales_csv_to_list(sales_a)
    data_sales_b = sales_xlsx_to_list(sales_b)
    data_brand = brand_xlsx_to_list(brand)

    # transform process
    data_sales_a = sales_transform(data_sales_a, data_brand)
    data_sales_b = sales_transform(data_sales_b, data_brand)

    # load process
    insert_to_sql(data_sales_a, 'sales_A.csv')
    insert_to_sql(data_sales_b, 'sales_B.xlsx')

    # reporting process
    sales_month_report()
    sales_product_report()


