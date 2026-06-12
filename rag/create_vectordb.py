import pandas as pd

from langchain_core.documents import Document

from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import HuggingFaceEmbeddings

df = pd.read_csv("../women_fashion.csv")

docs = []

for _, row in df.iterrows():

    text = f"""
    Product Name: {row['productDisplayName']}
    Category: {row['masterCategory']}
    Sub Category: {row['subCategory']}
    Article Type: {row['articleType']}
    Color: {row['baseColour']}
    Season: {row['season']}
    Occasion: {row['usage']}
    """

    doc = Document(

        page_content=text,

        metadata={

            "season": str(row["season"]),

            "occasion": str(row["usage"]),

            "article_type": str(row["articleType"])
        }
    )

    docs.append(doc)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory="women_fashion_db"
)

print("Vector Database Created")
print("Total Products:", len(docs))