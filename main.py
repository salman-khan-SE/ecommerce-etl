import pandas as pd
from extract import extract
from transform import transform
from load import load
import logging 

logging.basicConfig(level=logging.INFO,filename='etl.log',filemode='w',format="%(asctime)s:%(levelname)s:%(message)s")


def main():
    logging.info('pipeline started')
    raw_data = extract()
    df = transform(raw_data)
    load(df)

if __name__ == '__main__':

    main()
    logging.info('pipeline completed')