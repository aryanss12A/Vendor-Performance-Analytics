from sqlalchemy import create_engine
import logging
import time
logging.basicConfig(
    filename="log/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

def ingest_db(df, table_name, engine):
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)
engine=create_engine('sqlite:///inventory_db')

# Then use it
import os
import pandas as pd
start_time = time.time()
for file in os.listdir('data'):
    if file.endswith('.csv'):
        df = pd.read_csv('data/' + file)
        logging.info(f'Ingesting {file} in db')
        ingest_db(df, file[:-4], engine)
end_time = time.time()
total_time = (end_time - start_time)/60
logging.info('Ingestion Completed')
logging.info(f'\nTotal Time Taken: {total_time}minutes')


def load_raw_data():
    print("Loading raw data...")

if __name__ == "__main__":
    load_raw_data()
