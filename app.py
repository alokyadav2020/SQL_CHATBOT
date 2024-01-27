import streamlit as st
from src.SQLCHAT import Respons_From_Model

st.title("MySql: Database Q&A 👕")

question = st.text_input("Question: ")

if question:
    chain = Respons_From_Model()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)