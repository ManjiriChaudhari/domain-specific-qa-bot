import os
import faiss
import numpy as np
import streamlit as st

from sentence_transformers import SentenceTransformer


# -----------------------------
# Load Knowledge Base
# -----------------------------

@st.cache_data
def load_knowledge_base(file_path="data/trading_knowledge.txt"):

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found.")

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    return text


# -----------------------------
# Split into Chunks
# -----------------------------

def get_chunks(text):

    return [
        chunk.strip()
        for chunk in text.split("\n\n")
        if chunk.strip()
    ]


# -----------------------------
# Load Embedding Model
# -----------------------------

@st.cache_resource
def load_embedding_model():

    return SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )


# -----------------------------
# Load FAISS Index
# -----------------------------

@st.cache_resource
def load_faiss():

    return faiss.read_index(
        "models/trading_index.faiss"
    )


# -----------------------------
# Retrieve Context
# -----------------------------

def retrieve_context(question, k=3):

    text = load_knowledge_base()

    chunks = get_chunks(text)

    model = load_embedding_model()

    index = load_faiss()

    embedding = model.encode([question])

    distances, indices = index.search(
        np.array(embedding).astype("float32"),
        k
    )

    contexts = []

    for idx in indices[0]:

        if idx < len(chunks):

            contexts.append(chunks[idx])

    return contexts


# -----------------------------
# Suggested Questions
# -----------------------------

def suggested_questions():

    return [

        "What is RSI?",

        "Explain MACD.",

        "What is Stop Loss?",

        "What is Swing Trading?",

        "Bull vs Bear Market",

        "Explain Technical Analysis"

    ]
