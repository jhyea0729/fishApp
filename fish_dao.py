import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import sqlalchemy as db
from fish_api import getTrains, getTestes

engine = db.create_engine("mariadb+mariadbconnector://python:python1234@127.0.0.1:3306/pythondb")

def train_Insert():
    trains = getTrains()
    trains.to_sql("train", engine, index=False, if_exists="replace")

def train_Select():
    df = pd.read_sql(sql="select * from train", con=engine)
    print(df)

def test_Insert():
    testes = getTestes()
    testes.to_sql("test", engine, index=False, if_exists="replace")

def test_Select():
    df = pd.read_sql(sql="select * from test", con=engine)
    print(df)


train_Insert()
test_Insert()