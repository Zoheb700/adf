import sys
import pymysql

........

rds_host  = "samadahad.chgw8qg20c5u.us-east-1.rds.amazonaws.com"
name = "samadahad"
password = "Anam786"
db_name = "samadahad"
conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)

with conn.cursor() as cur:
   query="CALL public.usp_citydata_1"
   cur.execute(query)
   conn.commit()
   cur.close()