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

def transform_data(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    
    df = pd.merge(df1, df2, on="STORE_CODE", how="inner")
    df = df[["STORE_NAME", "BUSINESS_NAME", "SALES_VALUE", "SALES_QTY"]]

    df = (
        df.groupby(["STORE_NAME", "BUSINESS_NAME"])[["SALES_VALUE", "SALES_QTY"]]
        .sum()
        .reset_index()
    )

    df["TM"] = (df["SALES_VALUE"] / df["SALES_QTY"]).round(2)

    df = df.rename(columns={
        "STORE_NAME": "Loja",
        "BUSINESS_NAME": "Categoria"
    })

    df = df[["Loja", "Categoria", "TM"]].sort_values(by="Loja", ascending=True).reset_index(drop=True)

    return df

def retrieve_data(
    date: list[str]
):
    
    query_1 = """
        SELECT
            STORE_CODE,
            STORE_NAME,
            START_DATE,
            END_DATE,
            BUSINESS_NAME,
            BUSINESS_CODE
        FROM data_store_cad
    """

    query_2 = """
        SELECT
            STORE_CODE,
            DATE,
            SALES_VALUE,
            SALES_QTY
        FROM data_store_sales
    """

    if date:
        query_2 += f" WHERE DATE BETWEEN '{date[0]}' AND '{date[1]}'"

    engine = db_engine(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port
    )

    with engine.connect() as conn:
        df1 = pd.read_sql(query_1, engine)
        df2 = pd.read_sql(query_2, engine)

    df_final = transform_data(df1, df2)
    print(df_final.head())

    return df_final

    
if __name__ == "__main__":
    requested_date = ['2019-01-01', '2019-12-31']
    
    retrieve_data(
        date = requested_date
    )