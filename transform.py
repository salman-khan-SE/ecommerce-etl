import pandas as pd
import logging

def transform(raw_data):
    try:
        logging.info('transformation started')

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
        duplicates = raw_data.duplicated().sum()
        if duplicates > 0:
            logging.warning(f'{duplicates} Duplicated records found')
        raw_data = raw_data.drop_duplicates()

        missing_names = raw_data['customer_name'].isnull().sum()
        if missing_names > 0:
            logging.warning(f'{missing_names} Some Customer Names are missing')
        raw_data['customer_name'] = raw_data['customer_name'].fillna('unknown')

        # profit margin
        raw_data['profit_margin'] = raw_data['Profit'] / raw_data['sales']
        # datetime
        raw_data['order_date']= pd.to_datetime(raw_data['order_date'])
        
        
        if (raw_data['sales']<0).any():
            raise ValueError('Negative values in sales')
        if (raw_data['Quantity'] < 0).any():
            raise ValueError('Invalid quantity found')
        logging.info('data transformed')
        return raw_data
    
    except Exception as e:
        logging.error(f'transformtion failed{e}')
        raise