import os
from sqlalchemy import create_engine
import pandas as pd
import argparse
from dotenv import load_dotenv, find_dotenv
import detcode

load_dotenv(find_dotenv())

arg = argparse.ArgumentParser()
engine = create_engine(os.getenv('DATABASE_URI'))


def import_file(arg):
    encoding = detcode.detectCode(arg.file)
    df = pd.read_csv(arg.file, sep=',', encoding=encoding)
    df.columns = [c.lower() for c in df.columns]
    df.to_sql(arg.table, engine)


if __name__ == '__main__':
    arg.add_argument("--file", "-f", default="",
                     type=str, help="the file path.")
    arg.add_argument("--table", "-t", default="",
                     type=str, help="the table name.")
    args = arg.parse_args()
    import_file(args)
