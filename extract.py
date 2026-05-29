import pandas as pd
import logging

def extract():
    try:
        logging.info('extraction started')
        raw_data = pd.read_csv('data/Superstore.csv',encoding='latin1')
        logging.info('extraction successful')
        return raw_data
    except Exception as e:
        logging.info(f'extraction failed{e}')
        raise

