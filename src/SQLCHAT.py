import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from dotenv import load_dotenv
# from src.config import DataBaseCOnnection 

load_dotenv() 

# db =DataBaseCOnnection()


def DbConnection():
      db_user = "root"
      db_password = "admin"
      db_host = "localhost" #"DESKTOP-KHE50IO"
      db_name = "classicmodels"
      db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")
      print("from config file")
    
      return db

def Respons_From_Model():


    llm = ChatGoogleGenerativeAI(model='models/gemini-pro',google_api_key=os.getenv("GOOGLE_API_KEY"))
    print(llm)

    db = DbConnection()

    toolkit = SQLDatabaseToolkit(db=db,llm=llm)

    agent_executor = create_sql_agent(llm=llm, toolkit=toolkit, handle_parsing_errors=True, verbose=True)

    #respone = agent_executor.run(question)

    return agent_executor
