from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="rag/women_fashion_db",
    embedding_function=embedding_model
)

occasion_mapping = {

    "Office": "Formal",

    "Party": "Party",

    "Wedding": "Ethnic",

    "Gym": "Sports",

    "College": "Casual",

    "Casual": "Casual"
}


def retrieve_fashion(
    season,
    occasion
):

    mapped_occasion = occasion_mapping.get(
        occasion,
        "Casual"
    )

    query = f"""
    Season: {season}
    Occasion: {mapped_occasion}
    """

    docs = db.similarity_search(
        query,
        k=5
    )

    return docs