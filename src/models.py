import faiss
import streamlit as st

from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

from src.config import (
    EMBEDDING_MODEL,
    LLM_MODEL,
    FAISS_INDEX
)

# ----------------------------------------
# Load Embedding Model
# ----------------------------------------

@st.cache_resource
def load_embedding_model():

    return SentenceTransformer(
        EMBEDDING_MODEL
    )


# ----------------------------------------
# Load FLAN-T5 Model
# ----------------------------------------

@st.cache_resource
def load_generator():

    tokenizer = AutoTokenizer.from_pretrained(
        LLM_MODEL
    )

    model = AutoModelForSeq2SeqLM.from_pretrained(
        LLM_MODEL
    )

    return tokenizer, model


# ----------------------------------------
# Load FAISS Index
# ----------------------------------------

@st.cache_resource
def load_index():

    return faiss.read_index(
        str(FAISS_INDEX)
    )

