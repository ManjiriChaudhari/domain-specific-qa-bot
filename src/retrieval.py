import faiss
import numpy as np

from src.config import (
    FAISS_INDEX,
    TOP_K
)

from src.utils import (
    load_documents,
    split_into_chunks
)

from src.models import (
    load_embedding_model,
    load_index
)

# ----------------------------------------
# Build FAISS Index
# ----------------------------------------

def build_index():

    embedding_model = load_embedding_model()

    text = load_documents()

    chunks = split_into_chunks(text)

    embeddings = embedding_model.encode(
        chunks,
        convert_to_numpy=True
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(
        embeddings.astype("float32")
    )

    faiss.write_index(
        index,
        str(FAISS_INDEX)
    )

    return index, chunks


# ----------------------------------------
# Retrieve Context
# ----------------------------------------

def retrieve_context(question):

    embedding_model = load_embedding_model()

    index = load_index()

    text = load_documents()

    chunks = split_into_chunks(text)

    question_embedding = embedding_model.encode(
        [question],
        convert_to_numpy=True
    )

    distances, indices = index.search(
        question_embedding.astype("float32"),
        TOP_K
    )

    contexts = []

    scores = []

    for score, idx in zip(
        distances[0],
        indices[0]
    ):

        contexts.append(chunks[idx])

        similarity = round(
            100 / (1 + score),
            2
        )

        scores.append(similarity)

    return contexts, scores
