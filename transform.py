import pandas as pd
import logging

def transform(raw_data):
    try:
        logging.info('transformation started')
        raw_data = raw_data.drop_duplicates()

        raw_data['Customer Name'] = raw_data['Customer Name'].fillna('unknown')

        # renaming columns
        raw_data.rename(columns={'Order Date' :'order_date',
                                 'Sales':'sales',
                                 'Customer Name':'customer_name',
                                 'Row ID' : 'row_id',
                                 'Order ID' : 'order_id',
                                 'Ship Date' : 'ship_date',
                                 'Ship Mode' : 'ship_mode',
                                 'Customer ID' : 'customer_id',
                                 'Postal Code'  : 'postal_code',
                                 'Product ID' : 'product_id',
                                 'Sub-Category' : 'sub_category',
                                 'Product Name' : 'product_name'
                                },inplace=True)
        # profit margin
        raw_data['profit_margin'] = raw_data['Profit'] / raw_data['sales']
        # datetime
        raw_data['order_date']= pd.to_datetime(raw_data['order_date'])
        # sales by caegory
        category_sales=raw_data.groupby('Category').agg({
        'sales':'sum',
        'Profit':'sum'
        }).reset_index()
        logging.info('data transformed')
        return raw_data,category_sales
    except Exception as e:
        logging.error(f'transformtion failed{e}')
        raise