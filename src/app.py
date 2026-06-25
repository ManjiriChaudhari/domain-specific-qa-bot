import streamlit as st
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

st.set_page_config(
    page_title="Trading RAG Assistant",
    page_icon="📈",
    layout="wide"
)
with st.sidebar:
    st.header("📊 About")
    
    st.write(
        """
        Trading RAG Assistant

        - FAISS Vector Search
        - MiniLM Embeddings
        - FLAN-T5 Generation
        - Streamlit UI
        """
    )
    st.divider()
    
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()


# ----------------------------
# Page Title
# ----------------------------

st.title("📈 Trading RAG Assistant")
st.markdown(
    """
    Ask questions about:

    • RSI
    • MACD
    • Stop Loss
    • Swing Trading
    • Bull Market
    • Bear Market
    • Technical Analysis
    """
)
st.write("Ask trading and finance related questions")

# ----------------------------
# Load Knowledge Base
# ----------------------------

with open("data/trading_knowledge.txt", "r") as f:
    text = f.read()

chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]

# ----------------------------
# Load Embedding Model
# ----------------------------

@st.cache_resource
def load_embedding_model():
    return SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )

embedding_model = load_embedding_model()

# ----------------------------
# Load FAISS Index
# ----------------------------

index = faiss.read_index(
    "models/trading_index.faiss"
)

# ----------------------------
# Load FLAN-T5
# ----------------------------

@st.cache_resource
def load_generator():

    model_name = "google/flan-t5-base"

    tokenizer = AutoTokenizer.from_pretrained(
        model_name
    )

    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_name
    )

    return tokenizer, model

tokenizer, model = load_generator()

# ----------------------------
# Retrieval Function
# ----------------------------

def retrieve_context(query, k=3):

    query_embedding = embedding_model.encode(
        [query]
    )

    D, I = index.search(
        np.array(query_embedding).astype("float32"),
        k
    )

    contexts = [chunks[idx] for idx in I[0]]

    return "\n".join(contexts)
# ----------------------------
# RAG Function
# ----------------------------

def ask_trading_bot(question):

    context = retrieve_context(question)

    prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=50
    )
    
    outputs = model.generate(
        **inputs,
        max_new_tokens=100,
        temperature=0.7
    )

    return answer, context

# ----------------------------
# User Interface
# ----------------------------

# Initialize chat history

if "messages" not in st.session_state:
    st.session_state.messages = []

# User input

question = st.chat_input(
    "Ask a trading question..."
)

# Process question

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.spinner("Thinking..."):
        answer, context = ask_trading_bot(question)
        
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "context": context
        }
    )

# Display chat history

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.write(msg["content"])

        if msg["role"] == "assistant":

            if "context" in msg:
                with st.expander("📚 Retrieved Knowledge"):
                    st.code(msg["context"])
                    
st.markdown("---")
st.caption(
    "Built using Streamlit, FAISS, Sentence Transformers and FLAN-T5"
)
