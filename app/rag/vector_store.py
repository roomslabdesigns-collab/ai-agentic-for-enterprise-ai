import faiss
import numpy as np


def create_faiss_index(embeddings):

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    return index

def search(index, query_embedding, k=3):

    distances, indices = index.search(
        query_embedding,
        k
    )

    return distances, indices

import faiss
import pickle


def save_index(index, path):

    faiss.write_index(
        index,
        path
    )


def load_index(path):

    return faiss.read_index(path)


def save_chunks(chunks, path):

    with open(
        path,
        "wb"
    ) as file:

        pickle.dump(
            chunks,
            file
        )


def load_chunks(path):

    with open(
        path,
        "rb"
    ) as file:

        return pickle.load(file)