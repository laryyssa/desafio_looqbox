import ast
from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()

host = os.getenv("DB_IP")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
schema = os.getenv("DB_SCHEMA")
database = os.getenv("DB_NAME")
port = int(os.getenv("DB_PORT"))

def db_engine(
    host: str,
    user: str,
    password: str,
    database: str,
    port: int
):
    engine = create_engine(
        f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    )
    return engine


def retrieve_data(
    product_code: int,
    store_code : int,
    date: list[str]
):
    
    query = """
        SELECT *
        from data_product_sales dps
    """

    if product_code:
        query += f"WHERE dps.PRODUCT_CODE = {product_code}"

    if store_code:
        query += f" AND dps.STORE_CODE = {store_code}"

    if date:
        dates_sql = ", ".join(f"'{d.strip()}'" for d in date)
        query += f" AND dps.DATE IN ({dates_sql})"

    
    engine = db_engine(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port
    )
    with engine.connect() as conn:
        df = pd.read_sql(query, engine)

    print(df.head())

    return df

def exemple_usage():
    product_code = input("Enter product code: ")
    store_code = input("Enter store code: ")

    date = input("Enter dates ([YYYY-MM-DD, YYYY-MM-DD]): ")
    date = ast.literal_eval(date)
    print(date)

    retrieve_data(product_code, store_code, date)
    
if __name__ == "__main__":
    exemple_usage()