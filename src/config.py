from langchain.sql_database import SQLDatabase


class DataBaseCOnnection:

   def DbConnection():
      db_user = "root"
      db_password = "admin"
      db_host = "localhost" #"DESKTOP-KHE50IO"
      db_name = "classicmodels"
      db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")
      print("from config file")
    
      return db