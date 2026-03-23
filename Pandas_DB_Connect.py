import pandas as pd 
import pyodbc
import oracledb
from sqlalchemy import create_engine, types

engine = create_engine(
    "oracle+oracledb://system:Hieu2008@localhost:1522/?service_name=orcl"
)

conn_SSMS = pyodbc.connect(
    "DRIVER={ODBC driver 17 FOR SQL SERVER};"
    "SERVER=113.190.234.241,2597;"
    "DATABASE=eFUND_PMIS_TEST;"
    "UID=sa;"
    "PWD=m@tkhAumaychu@08:29"
)
for chunk in pd.read_sql('select * from tmat_dly_gsat_a',conn_SSMS,chunksize=30):
    print(f'Số dòng được đọc: {len(chunk)}')
    print(chunk)

conn_Oracle_1 = oracledb.connect(
    user='edw_user',
    password='123456',
    host='113.190.234.241',
    port='1521',
    service_name='dbwr'
)

conn_Oracle_2 = oracledb.connect(
    user='system',
    password='Hieu2008',
    host='localhost',
    port='1522',
    service_name='orcl'
)
for chunk in pd.read_sql('select * from tb04_g32_001_ttgs_01_a where rownum <= 50',conn_Oracle_1,chunksize=25):
    print(chunk)