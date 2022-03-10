from sqlalchemy import create_engine
engine = create_engine('hive://localhost:10000/default')
import pandas as pd
df = pd.read_sql("SELECT * from table1", engine)
