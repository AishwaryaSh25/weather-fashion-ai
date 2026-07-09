from pathlib import Path
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Project root directory
BASE_DIR = Path(__file__).resolve().parent

# Database path
DB_PATH = BASE_DIR / "women_fashion_db"

print("Using DB:", DB_PATH)

db = Chroma(
    persist_directory=str(DB_PATH),
    embedding_function=embedding_model
)
print("Documents in DB:", db._collection.count())

docs = db.similarity_search("dress", k=5)
print("Retrieved:", len(docs))

for doc in docs:
    print(doc.page_content)

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
    Women's fashion.
    
    Season: {season}
    Occasion: {mapped_occasion}
    
    Find suitable:
    - Topwear
    - Bottomwear
    - Footwear
    - Accessories
    
    Return products appropriate for this season and occasion.
    """

    docs = db.similarity_search(
        query,
        k=20
    )
    print(f"\nRetrieved {len(docs)} docs")

    for i, doc in enumerate(docs):
        print(f"\nDoc {i+1}")
        print(doc.page_content[:300])


    return docs