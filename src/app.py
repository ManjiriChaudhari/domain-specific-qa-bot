
import streamlit as st

st.title("📈 Trading RAG Assistant")

st.write("Trading AI Assistant Project")

question = st.text_input("Ask a trading question")

if question:
    st.write("Answer:")
    st.write("Connect RAG pipeline here")
