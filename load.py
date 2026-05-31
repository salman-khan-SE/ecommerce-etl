import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import logging

load_dotenv()

user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')


engine = create_engine(
    f'mysql+pymysql://{user}:{password}@localhost/ecommerce_etl'
)

def load(df):
    try:
        logging.info('loading started')
        df.to_sql(
        'superstore',
        con=engine,
        if_exists='replace',
        index=False
        )
        logging.info('data loaded')
        return df
    except Exception as e:
        logging.error(f'loading failed{e}')
        raise

        